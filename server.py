from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


def main():
    app.run(
        debug=True,
        port=8000
    )

if __name__ == "__main__":
    main()
