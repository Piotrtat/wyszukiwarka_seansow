from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home_page():
    return render_template("main_paig.html")


if __name__ == '__main__':
    app.run()
