from flask import Flask, render_template, redirect, url_for, request, abort, flash
import forms

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, insert_sample  # (1.)

@app.route('/index')
@app.route('/')
def index():
    return render_template("base.html")
