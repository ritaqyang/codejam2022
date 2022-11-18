#!/usr/bin/python3
from flask import Flask

app = Flask('__name__')

@app.route('/animals')
def index():
  return f'''
  <h1> Adopt a Pet! </h1>
  <p>Browse through the links below to find your new furry friend:</P>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
  
  html = f'<h1>List of {pet_type}<h2>'
  return html 





