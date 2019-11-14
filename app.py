from flask import Flask, escape, request, abort, json
import pymorphy2
import json

app = Flask('grammar-unit')
morph = pymorphy2.MorphAnalyzer()

@app.route('/')
def index():
    # Params
    word = request.args.get("word", None)
    case = request.args.get("in_case", None)
    number = request.args.get("in_number", None)
    if not word:
        abort(422)

    # Getting word's details
    parse = morph.parse(word)
    orig_case = parse[0].tag.case
    orig_number = parse[0].tag.number

    # Applying changes and build response
    if case or number:
        inflect = parse[0].inflect({
            case or orig_case,
            number or orig_number
        })
        resp = inflect.word
    else:
        resp = []
        for i in parse:
            resp.append({
                'normal_form': i.normal_form,
                'part_of_speech': i.tag.POS,
                'case': i.tag.case,
                'gender': i.tag.gender,
                'number': i.tag.number,
                'tense': i.tag.tense,
                'score': i.score
            })

    # Make a response
    return json.dumps({
        'code': 200,
        'message': resp
    }, ensure_ascii=False)

# Error handling
@app.errorhandler(422)
def unprocessable_entity(error):
    return '[422] Unprocessable Entity: looks like a required parameter was missing!', 422

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
