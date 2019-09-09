from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return render.template("site.html") # rander.tamplate is importing an external file.
if __name__ == "__main__":
    app.run(debug=True)
