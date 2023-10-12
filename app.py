from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Главная страница</h1>'\

@app.route('/about')
def about():
    return '<h1>Инфо</h1>'


if __name__ == '__main__':
    app.run(debug=True)
