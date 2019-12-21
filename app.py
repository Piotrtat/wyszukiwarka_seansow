from flask import Flask, render_template
import moje
from movie_list_func import run_search, final
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("main_paig.html")


@app.route('/selected')
def all_movies():
    filmy = run_search()
    return render_template("all_movies.html", len=len(filmy), filmy=filmy)


@app.route('/selected_movie')
def research_movie():
    movie = 'cos'
    return render_template("one_movie.html", one_movie=movie)


@app.route('/helios_page')
def reservation_mode():
    return render_template("reserve_movie.html")


@app.route('/')
def index():
    return render_template(
        'index.html',
        lista_button=movies4)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = requests.form.get('comp_select')
    return(str(select)) # just to see what select is


if __name__ == '__main__':
    app.run()
