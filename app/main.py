from app import main_app
from flask import render_template

@main_app.route("/")
def main() :
    return render_template("main.html")