from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/index/')
def hello_world():
  return render_template('index.html', text = "booty")

if __name__ == '__main__':
  app.debug = True
  app.run()