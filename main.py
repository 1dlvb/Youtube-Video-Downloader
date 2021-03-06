from flask import Flask, render_template, redirect, url_for, request
from downloader import YtDownloader, preview_image
app = Flask(__name__)

yt = YtDownloader()


@app.route("/home", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        link = request.form["link"]
        yt.initialisation(link)
        title = yt.title()
        preview_img = preview_image(yt.video_id())
        print(title)
        print(preview_img)

    return render_template("index.html", link=link)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/download")
def download():
    return render_template("download.html")

if __name__ == "__main__":
    app.run(debug=True)
