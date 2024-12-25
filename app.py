# app.py
# -*- coding: utf-8 -*-

import os
import threading
from flask import Flask
from flask_cors import CORS
from models import db
from router.routes_asset import bp_asset
from router.routes_file import bp_file
from router.routes_login import login_bp
from router.routes_material import bp_material
from router.routes_user import bp
from router.routes_permission import bp_permission
from router.routes_temperature import bp_temperature
from router.routes_sht40 import bp_sht40
from router.routes_sht30 import bp_sht30
from router.routes_fst import bp_fst
from router.routes_sgp30 import bp_sgp30
from router.routes_bme680 import bp_bme680
from router.routes_ltr329 import bp_ltr329
from router.routes_image import bp_image_server  # 导入刚才定义的 Blueprint


app = Flask(__name__)
app.config.from_object('config.Config')
app.config['SECRET_KEY'] = 'Thinkgo'
app.config['SESSION_TYPE'] = 'filesystem'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
CORS(app, supports_credentials=True)

db.init_app(app)

app.register_blueprint(bp)
app.register_blueprint(login_bp)
app.register_blueprint(bp_asset)
app.register_blueprint(bp_permission)
app.register_blueprint(bp_file)
app.register_blueprint(bp_temperature)
app.register_blueprint(bp_sht40)
app.register_blueprint(bp_sht30)
app.register_blueprint(bp_fst)
app.register_blueprint(bp_sgp30)
app.register_blueprint(bp_bme680)
app.register_blueprint(bp_ltr329)
app.register_blueprint(bp_material)
app.register_blueprint(bp_image_server)

# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

def run_ipv4():
    app.run(host='0.0.0.0', port=7777)

def run_ipv6():
    app.run(host='::', port=5000)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    threading.Thread(target=run_ipv4).start()
    threading.Thread(target=run_ipv6).start()
