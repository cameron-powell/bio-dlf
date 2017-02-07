from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404</h1>', 404


@app.errorhandler(500)
def internal_server_error(e):
    return '<h1>500</h1>', 500


if __name__ == '__main__':
    app.run(debug=True)
