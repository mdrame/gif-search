from flask import Flask, render_template, request
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
    return render_template("index.html")

@app.route('/legal')
def legal():

 # render_template() added our external html file found in the template folder of the same folder
    return render_template("legal.html")

@app.route('/about')
def about():

 # render_template() added our external html file found in the template folder of the same folder
    return render_template("about.html")

@app.route('/gif')
def gifFunc():

    # TODO: Extract query term from url
   user_Input = str(request.args.get('search'))


   # TODO: Make 'params' dict with query term and API key
   params = {"url": 'https://api.tenor.com/v1/', "query": user_Input,"key": "SNXP25MEWK1E", "limit": 10}

#testing API url
# curl "https://api.tenor.com/v1/search?q=query&key=SNXP25MEWK1E&limit=1"

   # TODO: Make an API call to Tenor using the 'requests' library
   api_requesting = requests.get(f"{params['url']}search?q={params['query']}&key={params['key']}&limit={params['limit']}")
   #gifs = api_requesting.json()

   # TODO: Get the first 10 results from the search results
   if api_requesting.status_code == 200:
       gif_list = json.loads(api_requesting.content)['results']
       #print(gif_List )
       #gifs['results'][0]['media'][0]['gif']['url']
   else:
       gif_list = [] #an empty list.




   # TODO: Render the 'index.html' template, passing the gifs as a named parameter

   return render_template("gif.html", gif_list=gif_list, user_Input=user_Input)

if __name__ == "__main__":
    app.run(debug=True)