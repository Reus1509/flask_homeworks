from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

MIN_AGE = 18


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/')
def index_post():
    age = int(request.form.get('age'))
    if age < MIN_AGE:
        return f'<script>alert("Вам нет еще 18 лет, вход запрещен!")</script>'
    return redirect("/succes")

@app.get('/succes')
def succes():
    return render_template("succes.html")

if __name__ == '__main__':
    app.run(debug=True)