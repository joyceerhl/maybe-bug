import flask
app = flask.Flask(__name__)

@app.route("/")
def home():
    resp = flask.Response("Hello world!")
    # resp.headers['Content-Security-Policy'] = 'frame-ancestors *;'
    return resp