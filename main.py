from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",title="Homepage")

@app.route("/about")
def about():
    return render_template("about.html", title ="About")

@app.route("/ministries")
def ministries():
    return render_template("ministries.html", title="Ministries")

@app.route("/activities")
def activities():
    return render_template("activities.html", title="Activities")

@app.route("/events")
def events():
    return render_template("events.html", title="Events")

@app.route("/give")
def give():
    return render_template("give.html", title="Give")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog")


if __name__ == "__main__":
    app.debug = True
    app.run()