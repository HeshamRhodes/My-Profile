from flask import Flask, render_template, url_for
from PIL import Image
#_____________________________________________________

profile = Flask(__name__)
#_____________________________________________________

@profile.route("/")
def main():
    return render_template("main.html", title = "Main profile")
#_____________________________________________________

@profile.route("/Experience")
def Experience():
    return render_template("experience.html", title = "My Experience",)
#_____________________________________________________

@profile.route("/Achievements")
def Achievements():
    return render_template("achievements.html", title = "My Achievements")
#_____________________________________________________

@profile.route("/Activities")
def Activities():
    return render_template("activities.html", title = "My Activities")
#_____________________________________________________

if __name__ == "__main__":
    profile.run(debug=True)