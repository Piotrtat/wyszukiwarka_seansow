from flask import Flask, render_template, request
from movie_list_func import run_search, current_movie_list

app = Flask(__name__)


@app.route('/')
def home_page():
    movies = current_movie_list()
    return render_template("main_paig.html", movies=movies)


@app.route('/selected')
def all_movies():
    filmy = run_search()
    return render_template("all_movies.html", len=len(filmy), filmy=filmy)


@app.route('/selected_movie', methods=['POST', 'GET'])
def research_movie():
    if request.method == "POST":
        movie = request.form['movies']
    return render_template("one_movie.html", one_movie=movie)


if __name__ == '__main__':
    app.run(debug=True)
