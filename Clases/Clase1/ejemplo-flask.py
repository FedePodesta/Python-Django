from flask import Flask

app = Flask (__name__)


@app.route ("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route ("/curso")
def hello_world():
    return "<h1>Hello Curso</h1>"




app.run()