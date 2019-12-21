from flask import Flask, render_template
from movie_list_func import run_search, final, current_movie_list

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template("main_paig.html", colours = current_movie_list())


@app.route('/selected')
def all_movies():
    filmy = run_search()
    return render_template("all_movies.html", len=len(filmy), filmy=filmy)


@app.route('/selected_movie')
def research_movie():
    movie = 'cos'
    return render_template("one_movie.html", one_movie=movie)


app.debug = True


@app.route('/a', methods=['GET'])
def dropdown():
    #current_movie_list()

    colours = current_movie_list()
    return render_template('main_paig.html', colours=colours)

if __name__ == '__main__':
    app.run()
