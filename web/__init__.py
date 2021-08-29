import os

from io import BytesIO
from flask import Flask, render_template, send_file, jsonify, request, redirect, url_for
from core import gcore

def wrap_resp(data, err):
    return jsonify({
        "data": data,
        "errcode": err
    })

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


def create_app():
    app = Flask(__name__)

    @app.route('/win/list')
    def winlist():
        return wrap_resp({"windows": gcore.win_list()}, 0)

    @app.route('/win/init')
    def wininit():
        win = request.args["win"]
        gcore.win_init(win, True)
        return wrap_resp(None, 0)

    @app.route('/win/size')
    def winsize():
        size = gcore.win_size()
        return wrap_resp(size, 0)


    @app.route('/win/click')
    def winclick():
        x = int(request.args["x"])
        y = int(request.args["y"])

        gcore.win_click(x, y)

        return wrap_resp(None, 0)

    @app.route('/img')
    def img():
        img = gcore.win_cap()
        return send_file(img, mimetype='image/png')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/live')
    def live():
        if not gcore.win_ok():
            return redirect('/')
        return render_template('live.html')

    return app
