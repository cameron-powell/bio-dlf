from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404</h1>', 404


@app.errorhandler(500)
def internal_server_error(e):
    return '<h1>500</h1>', 500


if __name__ == '__main__':
    app.run(debug=True)
