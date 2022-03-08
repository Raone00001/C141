# Import all modules
from flask import Flask, jsonify, request
import csv 

# All movies list
all_movies = []

# Put " encoding="utf-8" " in project as well
# Opening the csv file
with open('movies.csv', encoding="utf-8") as f:
    reader = csv.reader(f) # Reading the file
    data = list(reader) # Storing in data
    all_movies = data[1:] # Taking out the first index

# Creating the other lists for liked, disliked, and unwatched movies
liked_movies = []
disliked_movies = []
not_watched_movies = []

# Creating flask
app = Flask(__name__)

# Function for first api
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "Success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:] # Remove the movie from the all movies list
    liked_movies.append(movie) # Append the liked movie in that list
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:] # Remove the movie from the all movies list
    disliked_movies.append(movie) # Append the disliked movie in that list
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/not-watched-movie", methods=["POST"])
def did_not_watch_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:] # Remove the movie from the all movies list
    not_watched_movies.append(movie) # Append the not watched movie in that list
    return jsonify({
        "status": "Success"
    }), 201

if __name__ == "__main__":
    app.run()