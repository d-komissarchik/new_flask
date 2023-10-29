from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# app = Flask(__name__)
# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:////home/komisar/PycharmProjects/new_flask/newflask.db'
# #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# db = SQLAlchemy() # db intitialized here
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://test.db"
# db.init_app(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True);
    title = db.Column(db.String(300), nullable=False);
    text = db.Column(db.Text, nullable=False);


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
