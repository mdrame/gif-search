from flask import Flask
from flask import render_template

#todo: we nedda write a logic that will will check couple of charactor in the gif name and determine where they shoud be

app = Flask(__name__)


@app.route('/')
def func():

    return render_template('index.html') # render_template() added our external html file found in the template folder of the same folder



if __name__ == "__main__":
    app.run(debug=True)
