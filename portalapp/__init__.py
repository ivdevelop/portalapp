from flask import flask

app = Flask(__name__)
app.config.from_object(Config)