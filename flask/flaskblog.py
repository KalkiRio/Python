from flask import Flask, render_template
app=Flask(__name__)

posts = [
    {
        "title": "First Post",
        "author": "John Doe",
        "date": "2025-04-05",
        "content": "This is the content of the first post."
    },
    {
        "title": "Second Post",
        "author": "Jane Doe",
        "date": "2025-04-04",
        "content": "This is the content of the second post."
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")


if __name__=="__main__":
    app.run(debug=True)