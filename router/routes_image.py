from flask import Blueprint, send_from_directory, abort
import os

# 创建一个 Blueprint 用于图片服务
bp_image_server = Blueprint('image_server', __name__)

# 获取 upload 文件夹的路径
UPLOAD_FOLDER = 'uploads'
# @bp_permission.route('/api/permissions', methods=['GET'])
# 路由：获取指定的图片
@bp_image_server.route('/images/<filename>',methods=['GET'])
def get_image(filename):
    # 检查文件是否存在
    try:
        # 返回指定文件夹内的图片文件
        return send_from_directory(UPLOAD_FOLDER, filename)
    except FileNotFoundError:
        # 如果文件没有找到，返回 404 错误
        abort(404)

