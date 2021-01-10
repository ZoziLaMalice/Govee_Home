from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
app = Flask(__name__)
Bootstrap(app)
colorpicker(app)
