from flask import Flask, render_template
from controllers.skaters_controller import skaters_blueprint
from controllers.lessons_controller import lessons_blueprint
from controllers.levels_controller import levels_blueprint
app = Flask(__name__)

app.register_blueprint(skaters_blueprint)
app.register_blueprint(lessons_blueprint)
app.register_blueprint(levels_blueprint)

@app.route('/')
def home():
    return render_template('home.jinja')

@app.route('/about')
def about():
    return render_template('about.jinja', title = "About Us")

@app.route('/error')
def error():
    return render_template('error.jinja', title = "Whoops!")

if __name__ == '__main__':
    app.run(debug=True)