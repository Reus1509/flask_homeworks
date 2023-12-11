from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run()