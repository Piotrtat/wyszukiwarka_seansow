from flask import Flask, render_template
import moje
from movie_list_func import run_search


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("main_paig.html")


@app.route('/selected')
def all_movies():
    filmy = run_search()
    return render_template("all_movies.html", filmy=filmy)


@app.route('/selected_movie')
def research_movie():
    movie = 'cos'
    return render_template("templates/one_movie.html", one_movie=movie)


if __name__ == '__main__':
    app.run()
