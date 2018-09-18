from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    movie_2 = get_random_movie()
    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    content2 = "<h1>Tomorrow's Movie</h1>"
    content2 += "<ul>"
    content2 += "<li>" + movie_2 + "</li>"
    content2 += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content + content2

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    movie_list = ["Pulp Fiction", "Four Rooms", "Reservoir Dogs","Matrix Trilogy","Gattaca",
    "K-Pax","City of Gods", "The Arrival"]
    
    return random.choice(movie_list)


app.run()
