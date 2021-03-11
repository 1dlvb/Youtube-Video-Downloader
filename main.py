from flask import Flask, render_template, redirect, url_for, request, jsonify, send_file
from io import BytesIO
from downloader import YtDownloader, preview_image
import os
import sqlite3 as sq
from random import randint

app = Flask(__name__)


yt = YtDownloader()
v_list = []
with sq.connect('database.db', check_same_thread=False) as db:
    cur = db.cursor()  # Cursor

    # budget table
    cur.execute("""CREATE TABLE IF NOT EXISTS data(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              link TEXT DEFAULT 0 NOT NULL

          )""")
    if cur.execute("SELECT Count() FROM data").fetchone()[0] <= 0:
        cur.execute("INSERT INTO data (link) VALUES (?)", [0])


@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/download/getfile/<name>')
def get_output_file(name):
    link = cur.execute("SELECT link FROM data").fetchone()[0]
    print(link)
    yt.initialize(link)
    data = yt.download()
    return send_file(BytesIO(data), attachment_filename=str(name)+'.mp4', as_attachment=True)


@app.route("/json", methods=['POST', 'GET'])
def json():
    req = request.get_json(force=True)
    if req['value'] == 'Download':
        link = req['link']
        yt.initialize(link)
        return "ok"
    else:
        return redirect(url_for(download))


@app.route("/download", methods=['POST', 'GET'])
def download():
    if request.method == 'POST':
        link = request.form["link"]
        yt.initialize(link)
        title = yt.title()
        preview_img = preview_image(yt.video_id())
        name = 'video' + str(randint(159, 999999999))
        cur.execute("UPDATE data SET link = (?)", [link])
        db.commit()
        return render_template("download.html", link=link, name=name, preview_img=preview_img, title=title)
    else:
        return "There was some kind of error"


if __name__ == "__main__":
    app.run(debug=False)
