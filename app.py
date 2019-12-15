from flask import Flask, render_template
import moje

app = Flask(__name__)
# Bootstrap(app)

@app.route('/')
def home_page():
    # tasks = moje
    return render_template("main_paig.html")


@app.route('/selected')
def research_movie():
    filmy = moje.moje()
    return render_template("all_movies.html", filmy=filmy)

if __name__ == '__main__':
    app.run()
