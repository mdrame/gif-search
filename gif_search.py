from flask import Flask, render_template,request
import requests
import json

# make another file or function in this page
# pass the user input into the function
# return the api_results
# ...
# or lookup how to add data into the request/ response object...


app = Flask(__name__)
gif_List = list()

@app.route('/')
def func():

 # render_template() added our external html file found in the template folder of the same folder
    return render_template('index.html')


@app.route('/gif')
def gifFunc():

    # TODO: Extract query term from url
   user_Input = str(request.args.get('search'))


   # TODO: Make 'params' dict with query term and API key
   params = {"url": 'https://api.tenor.com/v1/', "query": user_Input,"key": "SNXP25MEWK1E", "limit": 1}

#testing API url
# curl "https://api.tenor.com/v1/search?q=query&key=SNXP25MEWK1E&limit=1"

   # TODO: Make an API call to Tenor using the 'requests' library
   api_requesting = requests.get(f"{params['url']}search?q={params['query']}&key={params['key']}&limit={params['limit']}")
                                #
   api_results = api_requesting.json()
   # TODO: Get the first 10 results from the search results
   gif = api_results['results'][0]['media'][0]['gif']['url']


   # TODO: Render the 'index.html' template, passing the gifs as a named parameter

   return render_template("gif.html", gif=gif)


if __name__ == "__main__":
    app.run(debug=True)
