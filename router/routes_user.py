from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash
from models import db, User

bp = Blueprint('user', __name__)

def get_current_user():
    """ 获取当前登录用户的 ID """
    user_id = session.get('user_id')
    if user_id:
        return User.query.get(user_id)
    return None

@bp.route('/users', methods=['POST'])
def create_user():
    current_user = get_current_user()
    if not current_user:
        return jsonify({'message': 'User not logged in'}), 401

    # 你可能需要根据当前用户的权限来决定是否允许创建新用户
    # 例如，管理员可以创建新用户
    if current_user.role_id != 1:  # 假设 role_id 为 1 表示管理员
        return jsonify({'message': 'Permission denied'}), 403

    data = request.json
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(name=data['name'], email=data['email'], password=hashed_password, role_id=data['role_id'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/users', methods=['GET'])
def get_users():
    current_user = get_current_user()
    if not current_user:
        return jsonify({'message': 'User not logged in'}), 401

    # 示例：仅允许管理员用户获取所有用户列表
    if current_user.role_id != 1:
        return jsonify({'message': 'Permission denied'}), 403

    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    current_user = get_current_user()
    if not current_user:
        return jsonify({'message': 'User not logged in'}), 401

    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    # 示例：仅允许用户自己更新自己的信息
    if user.id != current_user.id and current_user.role_id != 1:
        return jsonify({'message': 'Permission denied'}), 403

    data = request.json
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    current_user = get_current_user()
    if not current_user:
        return jsonify({'message': 'User not logged in'}), 401

    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    # 示例：仅允许用户自己删除自己的账户
    if user.id != current_user.id and current_user.role_id != 1:
        return jsonify({'message': 'Permission denied'}), 403

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
