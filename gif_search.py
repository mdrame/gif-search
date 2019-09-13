from flask import Flask
from random import choice
from flask import render_template,request

compliments = ['Dope', 'Cool','LIT 🔥', 'Awesome']
#todo: we nedda write a logic that will will check couple of charactor in the gif name and determine where they shoud be

app = Flask(__name__)
gif_List = list()

@app.route('/')
def func():
    compliment = choice(compliments)
    return render_template('index.html', compliment=compliment)



     # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter


 # render_template() added our external html file found in the template folder of the same folder



if __name__ == "__main__":
    app.run(debug=True)
