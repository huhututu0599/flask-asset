from flask import Blueprint, request, jsonify
from models import db, User, Asset


bp_asset = Blueprint('asset', __name__)

# 查询所有资产
@bp_asset.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([{
        'id': asset.id,
        'name': asset.name,
        'value': asset.value,
        'owner_id': asset.owner_id
    } for asset in assets])

# 查询特定资产
@bp_asset.route('/assets/<int:asset_id>', methods=['GET'])
def get_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if asset is None:
        return jsonify({'message': 'Asset not found'}), 404
    return jsonify({
        'id': asset.id,
        'name': asset.name,
        'value': asset.value,
        'owner_id': asset.owner_id
    })

# 创建资产
@bp_asset.route('/assets', methods=['POST'])
def create_asset():

    data = request.json
    user = User.query.get(data['owner_id'])
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    new_asset = Asset(name=data['name'], value=data['value'], owner_id=data['owner_id'],barcode=data['barcode'])
    db.session.add(new_asset)
    db.session.commit()
    return jsonify({'message': 'Asset created successfully'}), 201

# 更新资产
@bp_asset.route('/assets/<int:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    data = request.json
    asset = Asset.query.get(asset_id)
    if asset is None:
        return jsonify({'message': 'Asset not found'}), 404
    asset.name = data['name']
    asset.value = data['value']
    asset.owner_id = data['owner_id']
    db.session.commit()
    return jsonify({'message': 'Asset updated successfully'})

# 删除资产
@bp_asset.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if asset is None:
        return jsonify({'message': 'Asset not found'}), 404
    db.session.delete(asset)
    db.session.commit()
    return jsonify({'message': 'Asset deleted successfully'})
