from flask import Flask, render_template, redirect, url_for, request, g
from downloader import YtDownloader, preview_image
app = Flask(__name__)

yt = YtDownloader()


@app.route("/home", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/download", methods=['POST', 'GET'])
def download():
    if request.method == 'POST':
        link = request.form["link"]
        yt.initialisation(link)
        title = yt.title()
        preview_img = preview_image(yt.video_id())

        return render_template("download.html",  preview_img=preview_img, title=title, link=link)
    else:
        return "There was some kind of error"


if __name__ == "__main__":
    app.run(debug=True)
