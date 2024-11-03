from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Could not shorten the URL."

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = ""
    if request.method == "POST":
        long_url = request.form.get("long_url")
        short_url = shorten_url(long_url)
    return render_template("index.html", short_url=short_url)

if __name__ == "__main__":
    app.run(debug=True)
