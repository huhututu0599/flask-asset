# from flask import Blueprint, request, jsonify, session
# from werkzeug.security import check_password_hash
# from models import User, db
#
# login_bp = Blueprint('login', __name__)
#
# def get_user_by_credentials(email, name):
#     """根据邮箱或用户名查找用户"""
#     if email:
#         return User.query.filter_by(email=email).first()
#     elif name:
#         return User.query.filter_by(name=name).first()
#     return None
#
# # @login_bp.route('/login', methods=['POST'])
# # def login():
# #     try:
# #         data = request.json
# #         email = data.get('email')
# #         name = data.get('name')
# #         password = data.get('password')
# #
# #         if not password or (not email and not name):
# #             return jsonify({'message': 'Missing credentials'}), 400
# #
# #         user = get_user_by_credentials(email, name)
# #
# #         if user and check_password_hash(user.password, password):
# #             # 登录成功，将用户 ID 和角色 ID 存储到 session 中
# #             session['user_id'] = user.id
# #             session['role_id'] = user.role_id
# #             return jsonify({'message': 'Login successful', 'role_id': user.role_id}), 200
# #         else:
# #             return jsonify({'message': 'Invalid credentials'}), 401
# #     except Exception as e:
# #         print(f"Error in login: {e}")  # 记录错误日志
# #         return jsonify({'message': 'Internal Server Error'}), 500
# # @login_bp.route('/check_login', methods=['GET'])
# # def check_login():
# #     try:
# #         if 'user_id' in session:
# #             print(f"Session data: {session}")  # 记录 session 数据
# #             return jsonify({'logged_in': True, 'user_id': session['user_id']}), 200
# #         else:
# #             return jsonify({'logged_in': False}), 401
# #     except Exception as e:
# #         print(f"Error in check_login: {e}")
# #         return jsonify({'message': 'Internal Server Error'}), 500
# @login_bp.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('email')
#     password = data.get('password')
#
#     # 在这里添加你的用户验证逻辑
#     if username == 'admin@123.com' and password == 'admin':  # 示例验证
#         session['user'] = username  # 将用户存储到 session
#         return jsonify(message='Login successful'), 200
#
#     return jsonify(message='Login failed'), 401
#
#
# @login_bp.route('/check_login', methods=['GET'])
# def check_login():
#     if 'user' in session:
#         return jsonify(logged_in=True)
#     return jsonify(logged_in=False)
#
#
# @login_bp.route('/logout', methods=['POST'])
# def logout():
#     try:
#         # 清除 session 中的用户信息
#         session.pop('user_id', None)
#         session.pop('role_id', None)
#         return jsonify({'message': 'Logout successful'}), 200
#     except Exception as e:
#         print(f"Error in logout: {e}")
#         return jsonify({'message': 'Internal Server Error'}), 500


from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash
from models import User, db

login_bp = Blueprint('login', __name__)

def get_user_by_credentials(email, name):
    """根据邮箱或用户名查找用户"""
    if email:
        return User.query.filter_by(email=email).first()
    elif name:
        return User.query.filter_by(name=name).first()
    return None
#
# @login_bp.route('/login', methods=['POST'])
# def login():
#     try:
#         data = request.json
#         email = data.get('email')
#         name = data.get('name')
#         password = data.get('password')
#
#         if not password or (not email and not name):
#             return jsonify({'message': 'Missing credentials'}), 400
#
#         user = get_user_by_credentials(email, name)
#
#         if user and check_password_hash(user.password, password):
#             # 登录成功，将用户 ID 和角色 ID 存储到 session 中
#             session['user_id'] = user.id
#             session['role_id'] = user.role_id
#             return jsonify({'message': 'Login successful', 'role_id': user.role_id}), 200
#         else:
#             return jsonify({'message': 'Invalid credentials'}), 401
#     except Exception as e:
#         print(f"Error in login: {e}")  # 记录错误日志
#         return jsonify({'message': 'Internal Server Error'}), 500

@login_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')

        if not password or (not email and not name):
            return jsonify({'message': 'Missing credentials'}), 400

        user = get_user_by_credentials(email, name)

        if user and check_password_hash(user.password, password):
            # 登录成功，将用户 ID 和角色 ID 存储到 session 中
            session['user_id'] = user.id
            session['role_id'] = user.role_id
            return jsonify({'message': 'Login successful', 'role_id': user.role_id}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        print(f"Error in login: {e}")  # 记录错误日志
        return jsonify({'message': 'Internal Server Error'}), 500
@login_bp.route('/check_login', methods=['GET'])
def check_login():
    try:
        if 'user_id' in session:
            print(f"Session data: {session}")  # 记录 session 数据
            return jsonify({'logged_in': True, 'user_id': session['user_id']}), 200
        else:
            return jsonify({'logged_in': False}), 401
    except Exception as e:
        print(f"Error in check_login: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@login_bp.route('/logout', methods=['POST'])
def logout():
    try:
        # 清除 session 中的用户信息
        session.pop('user_id', None)  # 从 session 中移除用户 ID
        session.pop('role_id', None)  # 如果有角色 ID 需要移除
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        print(f"Error in logout: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
