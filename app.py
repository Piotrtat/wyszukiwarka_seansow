from flask import Flask, render_template
import moje
from Flask_projekt.Movie_list_func import final, new_dict, new_dict2


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("main_paig.html")


@app.route('/selected')
def all_movies():
    filmy = final(new_dict, new_dict2)
    return render_template("all_movies.html", filmy=filmy)


@app.route('/selected_movie')
def research_movie():
    movie = "cos"
    return render_template("one_movie.html", one_movie=movie)


if __name__ == '__main__':
    app.run()
