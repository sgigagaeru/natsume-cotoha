import os
from bottle import get, post, request, static_file, run
from json import loads, dumps

@get('/reading/<filepath:path>')
def reading(filepath):
  return static_file(filepath, root=APP_ROOT)


@post('/get_dot')
def get_dot():
  global sentences

  line_number = int(request.forms.get("line_number"))
  night_number = request.forms.get("night_number")

  make_sentences(night_number)
  if(len(sentences[night_number]) <= line_number):
    line_number = 0

  next_line_number = line_number + 1
  if(len(sentences[night_number]) <= next_line_number):
    next_line_number = 0

  d = sentences[night_number][line_number]
  d['text_length'] = len(d['text'])
  d['next_line_number'] = next_line_number

  return dumps(d)


def make_sentences(night_number):
  if not sentences[night_number]:
    f = open(APP_ROOT + "json/" + night_number + ".json", "r")
    sentences[night_number] = loads(f.read())
    f.close()
  return

# ソースファイルの場所取得
APP_ROOT = os.path.dirname(os.path.abspath( __file__)) + "/"

sentences = {
  "1st-night" : [],
  "2nd-night" : [],
  "3rd-night" : [],
  "4th-night" : [],
  "5th-night" : [],
  "6th-night" : [],
  "7th-night" : [],
  "8th-night" : [],
  "9th-night" : [],
  "10th-night" : []
}

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
