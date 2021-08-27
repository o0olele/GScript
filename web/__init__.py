import os

from io import BytesIO
from flask import Flask, render_template, send_file, jsonify
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
        return wrap_resp(None, 0)

    @app.route('/win/click')
    def winclick():
        return wrap_resp(None, 0)

    @app.route('/img')
    def img():
        gcore.win_init("嘉定组集团董事峰会")
        img = gcore.win_cap()
        return serve_pil_image(img)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app