# grammar-unit
A minimalistic Python morphological analyzing / inflection (RU &amp; UK) microservice based on pymorphy2

## Installation and running

### From source
```bash
git clone https://github.com/k0rean-rand0m/grammar-unit.git
```

```bash
pip install pymorphy2 flask waitress
```

#### Running in dev
```bash
env FLASK_APP=app.py flask run
```
#### Running in production
```bash
python app.py
```

### Docker
#### Pull the image
```bash
docker pull docker.pkg.github.com/k0rean-rand0m/grammar-unit/grammar-unit:latest
```

#### Running in production
```bash
docker run -p 5000:5000 -d docker.pkg.github.com/k0rean-rand0m/grammar-unit/grammar-unit:latest
```

## Requesting
### Params
Get response via GET request to the api with params:
- **word** *required* - the word for a morphology analysis / mutation
- **in_case** - change case to a given
- **in_number** - change number to a given

Requesting with **word** parameter only will lead to a response with full morphology analysis of the given word.
Providing the request with **in_case** or/and **in_number** will resolve into a response with a mutated word.

#### Possible values
| in_case | in_number |
----------|------------
nomn | sing
gent | plur
datv
accs
ablt
loct

### Request samples

#### Request
http://localhost:5000/?word=сингулярность
#### Response
```json
{
  "code": 200,
  "message": [{
    "normal_form": "сингулярность",
    "part_of_speech": "NOUN",
    "case": "nomn",
    "gender": "femn",
    "number": "sing",
    "tense": null,
    "score": 0.5
  }, {
    "normal_form": "сингулярность",
    "part_of_speech": "NOUN",
    "case": "accs",
    "gender": "femn",
    "number": "sing",
    "tense": null,
    "score": 0.5
  }]
}
```
#### Request
http://localhost:5000/?word=сингулярность&in_case=gent
#### Response
```json
{
  "code": 200,
  "message": "сингулярности"
 }
```
