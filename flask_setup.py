from flask import Flask
import file_api

app = Flask("FlaskFileAPI")
file_api.register(app)