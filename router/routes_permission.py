from flask import Blueprint, request, jsonify
from models import db, Permission
from utils.util_session import get_user_role_id

bp_permission = Blueprint('permission', __name__)

@bp_permission.route('/api/permissions', methods=['GET'])
def get_permissions():
    user_role_id = get_user_role_id()  # 获取当前用户角色 ID
    permissions = db.session.query(Permission).filter(Permission.required_role_id <= user_role_id).all()
    return jsonify([p.name for p in permissions])

@bp_permission.route('/api/permissions', methods=['POST'])
def add_permission():
    data = request.json
    new_permission = Permission(name=data['name'], required_role_id=data['required_role_id'])
    db.session.add(new_permission)
    db.session.commit()
    return jsonify({'message': 'Permission added'}), 201

@bp_permission.route('/api/permissions/<int:id>', methods=['PUT'])
def update_permission(id):
    data = request.json
    permission = Permission.query.get(id)
    if permission:
        permission.name = data['name']
        permission.required_role_id = data['required_role_id']
        db.session.commit()
        return jsonify({'message': 'Permission updated'})
    return jsonify({'message': 'Permission not found'}), 404

@bp_permission.route('/api/permissions/<int:id>', methods=['DELETE'])
def delete_permission(id):
    permission = Permission.query.get(id)
    if permission:
        db.session.delete(permission)
        db.session.commit()
        return jsonify({'message': 'Permission deleted'})
    return jsonify({'message': 'Permission not found'}), 404
