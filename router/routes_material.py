# from flask import Blueprint, request, jsonify
# from models import db, MaterialInfo, MaterialInOut
# from datetime import datetime
# from sqlalchemy.exc import IntegrityError
# import os
# bp_material = Blueprint('material', __name__)
#
# # ---------------- Material Info CRUD ----------------
#
# # 添加新的物料信息
# # @bp_material.route('/material_info', methods=['POST'])
# # def add_material_info():
# #     data = request.json
# #     if not data:
# #         return jsonify({"error": "No data provided"}), 400
# #
# #     part_number = data.get('part_number')
# #     name = data.get('name')
# #     specification = data.get('specification')
# #     category = data.get('category')
# #
# #     if not all([part_number, name, specification]):
# #         return jsonify({"error": "Missing required fields"}), 400
# #
# #     new_material = MaterialInfo(
# #         part_number=part_number,
# #         name=name,
# #         specification=specification,
# #         category=category
# #     )
# #
# #     try:
# #         db.session.add(new_material)
# #         db.session.commit()
# #     except IntegrityError:
# #         db.session.rollback()
# #         return jsonify({"error": "Material with this part number already exists"}), 400
# #
# #     return jsonify({"message": "Material info added successfully"}), 201
# from werkzeug.utils import secure_filename
#
# # 设置文件上传的目录
# UPLOAD_FOLDER = '/uploads'  # 存放图片的文件夹
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # 允许的图片格式
#
# # 检查文件扩展名是否允许
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# # 添加新的物料信息
# @bp_material.route('/material_info', methods=['POST'])
# def add_material_info():
#     # 获取 JSON 数据
#     data = request.form  # 由于使用 multipart/form-data, 所以获取表单数据
#
#     part_number = data.get('part_number')
#     name = data.get('name')
#     specification = data.get('specification')
#     category = data.get('category')
#
#     # 获取上传的图片文件
#     image = request.files.get('image')
#
#     # 确保所有字段都存在
#     if not all([part_number, name, specification]):
#         return jsonify({"error": "Missing required fields"}), 400
#
#     # 检查图片文件是否存在并符合格式要求
#     if image and allowed_file(image.filename):
#         # 生成安全的文件名
#         filename = secure_filename(image.filename)
#         # 保存图片文件
#         image_path = os.path.join(UPLOAD_FOLDER, filename)
#         image.save(image_path)
#         image_url = f"/{image_path}"  # 假设前端通过这个 URL 请求图片
#     else:
#         return jsonify({"error": "Invalid image file"}), 400
#
#     # 创建新的物料对象
#     new_material = MaterialInfo(
#         part_number=part_number,
#         name=name,
#         specification=specification,
#         category=category,
#         image_url=image_url  # 保存图片路径
#     )
#
#     try:
#         db.session.add(new_material)
#         db.session.commit()
#         return jsonify({"message": "Material info added successfully"}), 201
#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({"error": "Material with this part number already exists"}), 400
#
#
#
# # 获取所有物料信息
# @bp_material.route('/material_info', methods=['GET'])
# def get_all_material_info():
#     materials = MaterialInfo.query.all()
#     result = [
#         {
#             "id": material.id,
#             "part_number": material.part_number,
#             "name": material.name,
#             "specification": material.specification,
#             "category": material.category
#         }
#         for material in materials
#     ]
#     return jsonify(result), 200
#
# # 更新指定料号的物料信息
# @bp_material.route('/material_info/<part_number>', methods=['PUT'])
# def update_material_info(part_number):
#     data = request.json
#     material = MaterialInfo.query.filter_by(part_number=part_number).first()
#     if not material:
#         return jsonify({"error": "Material not found"}), 404
#
#     material.name = data.get('name', material.name)
#     material.specification = data.get('specification', material.specification)
#     material.category = data.get('category', material.category)
#
#     db.session.commit()
#     return jsonify({"message": "Material info updated successfully"}), 200
#
# # 删除指定料号的物料信息
# @bp_material.route('/material_info/<part_number>', methods=['DELETE'])
# def delete_material_info(part_number):
#     material = MaterialInfo.query.filter_by(part_number=part_number).first()
#     if not material:
#         return jsonify({"error": "Material not found"}), 404
#
#     db.session.delete(material)
#     db.session.commit()
#     return jsonify({"message": "Material info deleted successfully"}), 200
#
# # ---------------- Material In/Out CRUD ----------------
#
# # 添加新的出入库记录
# # @bp_material.route('/material_in_out', methods=['POST'])
# # def add_material_in_out():
# #     data = request.json
# #     if not data:
# #         return jsonify({"error": "No data provided"}), 400
# #
# #     part_number = data.get('part_number')
# #     status = data.get('status')  # "in" or "out"
# #     quantity = data.get('quantity')
# #     price = data.get('price')
# #
# #     if not all([part_number, status, quantity, price]):
# #         return jsonify({"error": "Missing required fields"}), 400
# #
# #     # 检查 part_number 是否存在于 material_info 表中
# #     material_info = MaterialInfo.query.filter_by(part_number=part_number).first()
# #     if not material_info:
# #         return jsonify({"error": "Part number does not exist"}), 404
# #
# #     new_in_out = MaterialInOut(
# #         part_number=part_number,
# #         status=status,
# #         quantity=quantity,
# #         price=price,
# #         timestamp=datetime.utcnow()
# #     )
# #
# #     db.session.add(new_in_out)
# #     db.session.commit()
# #     return jsonify({"message": "Material in/out record added successfully"}), 201
# @bp_material.route('/material_in_out', methods=['POST'])
# def add_material_in_out():
#     data = request.json
#     if not data:
#         return jsonify({"error": "No data provided"}), 400
#
#     part_number = data.get('part_number')
#     status = data.get('status')  # "in" or "out"
#     quantity = data.get('quantity')
#     price = data.get('price')
#
#     if not all([part_number, status, quantity, price]):
#         return jsonify({"error": "Missing required fields"}), 400
#
#     # 检查 part_number 是否存在于 material_info 表中
#     material_info = MaterialInfo.query.filter_by(part_number=part_number).first()
#     if not material_info:
#         return jsonify({"error": "Part number does not exist"}), 404
#
#     # 计算当前库存数量：累加所有入库记录，减去所有出库记录
#     total_in = db.session.query(db.func.sum(MaterialInOut.quantity)).filter_by(part_number=part_number, status='in').scalar() or 0
#     total_out = db.session.query(db.func.sum(MaterialInOut.quantity)).filter_by(part_number=part_number, status='out').scalar() or 0
#     current_stock = total_in - total_out
#
#     # 如果是出库操作，需要检查库存是否足够
#     if status == "out":
#         if current_stock < quantity:
#             return jsonify({"error": "Insufficient stock for this operation"}), 400
#
#     # 创建新的出入库记录
#     new_in_out = MaterialInOut(
#         part_number=part_number,
#         status=status,
#         quantity=quantity,
#         price=price,
#         timestamp=datetime.utcnow()
#     )
#
#     db.session.add(new_in_out)
#     db.session.commit()
#     return jsonify({"message": "Material in/out record added successfully"}), 201
#
#
# # 获取指定料号的所有出入库记录
# @bp_material.route('/material_in_out/<part_number>', methods=['GET'])
# def get_material_in_out(part_number):
#     records = MaterialInOut.query.filter_by(part_number=part_number).all()
#     if not records:
#         return jsonify({"error": "No records found"}), 404
#
#     result = [
#         {
#             "id": record.id,
#             "part_number": record.part_number,
#             "status": record.status,
#             "quantity": record.quantity,
#             "price": record.price,
#             "timestamp": record.timestamp.isoformat()
#         }
#         for record in records
#     ]
#     return jsonify(result), 200
#
# # 更新指定出入库记录
# @bp_material.route('/material_in_out/<int:id>', methods=['PUT'])
# def update_material_in_out(id):
#     data = request.json
#     in_out = MaterialInOut.query.get(id)
#     if not in_out:
#         return jsonify({"error": "Record not found"}), 404
#
#     in_out.status = data.get('status', in_out.status)
#     in_out.quantity = data.get('quantity', in_out.quantity)
#     in_out.price = data.get('price', in_out.price)
#     db.session.commit()
#
#     return jsonify({"message": "Material in/out record updated successfully"}), 200
#
# # 删除指定出入库记录
# @bp_material.route('/material_in_out/<int:id>', methods=['DELETE'])
# def delete_material_in_out(id):
#     in_out = MaterialInOut.query.get(id)
#     if not in_out:
#         return jsonify({"error": "Record not found"}), 404
#
#     db.session.delete(in_out)
#     db.session.commit()
#     return jsonify({"message": "Material in/out record deleted successfully"}), 200
#
# @bp_material.route('/inventory', methods=['GET'])
# #GET http://your_api_base_url/inventory
#
# def get_inventory():
#     # 查询 material_in_out 表中的入库和出库数据
#     in_records = db.session.query(MaterialInOut).filter(MaterialInOut.status == 'in').all()
#     out_records = db.session.query(MaterialInOut).filter(MaterialInOut.status == 'out').all()
#
#     # 初始化库存字典
#     inventory = {}
#
#     # 处理入库记录
#     for record in in_records:
#         if record.part_number in inventory:
#             inventory[record.part_number]['quantity'] += record.quantity
#         else:
#             # 根据料号查询物料信息
#             material_info = db.session.query(MaterialInfo).filter(MaterialInfo.part_number == record.part_number).first()
#             inventory[record.part_number] = {
#                 'name': material_info.name,
#                 'specification': material_info.specification,
#                 'category': material_info.category,
#                 'part_number': record.part_number,
#                 'quantity': record.quantity,
#                 'image_url':material_info.image_url
#             }
#
#     # 处理出库记录
#     for record in out_records:
#         if record.part_number in inventory:
#             inventory[record.part_number]['quantity'] -= record.quantity
#
#     # 过滤出库存大于0的记录
#     inventory = {k: v for k, v in inventory.items() if v['quantity'] > 0}
#
#     return jsonify(inventory), 200
#
#
# @bp_material.route('/inventory/search', methods=['GET'])
# #GET http://your_api_base_url/inventory/search?name=电阻
# def search_inventory():
#     # 从查询参数获取名称
#     name_query = request.args.get('name', '').lower()
#
#     # 查询 material_in_out 表中的入库和出库数据
#     in_records = db.session.query(MaterialInOut).filter(MaterialInOut.status == 'in').all()
#     out_records = db.session.query(MaterialInOut).filter(MaterialInOut.status == 'out').all()
#
#     # 初始化库存字典
#     inventory = {}
#
#     # 处理入库记录
#     for record in in_records:
#         if record.part_number in inventory:
#             inventory[record.part_number]['quantity'] += record.quantity
#         else:
#             # 根据料号查询物料信息
#             material_info = db.session.query(MaterialInfo).filter(
#                 MaterialInfo.part_number == record.part_number).first()
#             inventory[record.part_number] = {
#                 'name': material_info.name,
#                 'specification': material_info.specification,
#                 'category': material_info.category,
#                 'part_number': record.part_number,
#                 'quantity': record.quantity
#             }
#
#     # 处理出库记录
#     for record in out_records:
#         if record.part_number in inventory:
#             inventory[record.part_number]['quantity'] -= record.quantity
#
#     # 过滤出库存大于0的记录
#     inventory = {k: v for k, v in inventory.items() if v['quantity'] > 0}
#
#     # 根据名称模糊查询
#     filtered_inventory = {k: v for k, v in inventory.items() if name_query in v['name'].lower()}
#
#     return jsonify(filtered_inventory), 200


from flask import Blueprint, request, jsonify
from models import db, MaterialInfo, MaterialInOut
from datetime import datetime
from werkzeug.utils import secure_filename
import os
from sqlalchemy.exc import IntegrityError

bp_material = Blueprint('material', __name__)

# ---------------- 配置 ----------------
# 设置文件上传的目录
UPLOAD_FOLDER = 'uploads'  # 存放图片的文件夹
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # 允许的图片格式

# 检查文件扩展名是否允许
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 确保上传文件夹存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------------- Material Info CRUD ----------------

# 添加新的物料信息
@bp_material.route('/material_info', methods=['POST'])
def add_material_info():
    # 获取表单数据
    data = request.form  # 由于使用 multipart/form-data, 所以获取表单数据

    part_number = data.get('part_number')
    name = data.get('name')
    specification = data.get('specification')
    category = data.get('category')

    # 获取上传的图片文件
    image = request.files.get('image')

    # 确保所有字段都存在
    if not all([part_number, name, specification]):
        return jsonify({"error": "Missing required fields"}), 400

    # 检查图片文件是否存在并符合格式要求
    if image and allowed_file(image.filename):
        # 生成安全的文件名
        filename = secure_filename(image.filename)
        # 保存图片文件
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(image_path)
        # image_url = f"/{image_path}"  # 假设前端通过这个 URL 请求图片
        # 去掉文件路径中的上传文件夹部分（去掉前面的 uploads）
        image_url = filename  # 只返回文件名
    else:
        return jsonify({"error": "Invalid image file"}), 400

    # 创建新的物料对象
    new_material = MaterialInfo(
        part_number=part_number,
        name=name,
        specification=specification,
        category=category,
        image_url=image_url  # 保存图片路径
    )

    try:
        db.session.add(new_material)
        db.session.commit()
        return jsonify({"message": "Material info added successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Material with this part number already exists"}), 400


# 获取所有物料信息
@bp_material.route('/material_info', methods=['GET'])
def get_all_material_info():
    materials = MaterialInfo.query.all()
    result = [
        {
            "id": material.id,
            "part_number": material.part_number,
            "name": material.name,
            "specification": material.specification,
            "category": material.category,
            "image_url": material.image_url  # 返回图片 URL
        }
        for material in materials
    ]
    return jsonify(result), 200

# 更新指定料号的物料信息
@bp_material.route('/material_info/<part_number>', methods=['PUT'])
def update_material_info(part_number):
    data = request.json
    material = MaterialInfo.query.filter_by(part_number=part_number).first()
    if not material:
        return jsonify({"error": "Material not found"}), 404

    material.name = data.get('name', material.name)
    material.specification = data.get('specification', material.specification)
    material.category = data.get('category', material.category)

    db.session.commit()
    return jsonify({"message": "Material info updated successfully"}), 200

# 删除指定料号的物料信息
@bp_material.route('/material_info/<part_number>', methods=['DELETE'])
def delete_material_info(part_number):
    material = MaterialInfo.query.filter_by(part_number=part_number).first()
    if not material:
        return jsonify({"error": "Material not found"}), 404

    db.session.delete(material)
    db.session.commit()
    return jsonify({"message": "Material info deleted successfully"}), 200


# ---------------- Material In/Out CRUD ----------------

# 添加新的出入库记录
@bp_material.route('/material_in_out', methods=['POST'])
def add_material_in_out():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    part_number = data.get('part_number')
    status = data.get('status')  # "in" or "out"
    quantity = data.get('quantity')
    price = data.get('price')

    if not all([part_number, status, quantity, price]):
        return jsonify({"error": "Missing required fields"}), 400

    # 检查 part_number 是否存在于 material_info 表中
    material_info = MaterialInfo.query.filter_by(part_number=part_number).first()
    if not material_info:
        return jsonify({"error": "Part number does not exist"}), 404

    # 计算当前库存数量：累加所有入库记录，减去所有出库记录
    total_in = db.session.query(db.func.sum(MaterialInOut.quantity)).filter_by(part_number=part_number, status='in').scalar() or 0
    total_out = db.session.query(db.func.sum(MaterialInOut.quantity)).filter_by(part_number=part_number, status='out').scalar() or 0
    current_stock = total_in - total_out

    # 如果是出库操作，需要检查库存是否足够
    if status == "out":
        if current_stock < quantity:
            return jsonify({"error": "Insufficient stock for this operation"}), 400

    # 创建新的出入库记录
    new_in_out = MaterialInOut(
        part_number=part_number,
        status=status,
        quantity=quantity,
        price=price,
        timestamp=datetime.utcnow()
    )

    db.session.add(new_in_out)
    db.session.commit()
    return jsonify({"message": "Material in/out record added successfully"}), 201


# 获取指定料号的所有出入库记录
@bp_material.route('/material_in_out/<part_number>', methods=['GET'])
def get_material_in_out(part_number):
    records = MaterialInOut.query.filter_by(part_number=part_number).all()
    if not records:
        return jsonify({"error": "No records found"}), 404

    result = [
        {
            "id": record.id,
            "part_number": record.part_number,
            "status": record.status,
            "quantity": record.quantity,
            "price": record.price,
            "timestamp": record.timestamp.isoformat()
        }
        for record in records
    ]
    return jsonify(result), 200

# 更新指定出入库记录
@bp_material.route('/material_in_out/<int:id>', methods=['PUT'])
def update_material_in_out(id):
    data = request.json
    in_out = MaterialInOut.query.get(id)
    if not in_out:
        return jsonify({"error": "Record not found"}), 404

    in_out.status = data.get('status', in_out.status)
    in_out.quantity = data.get('quantity', in_out.quantity)
    in_out.price = data.get('price', in_out.price)
    db.session.commit()

    return jsonify({"message": "Material in/out record updated successfully"}), 200

# 删除指定出入库记录
@bp_material.route('/material_in_out/<int:id>', methods=['DELETE'])
def delete_material_in_out(id):
    in_out = MaterialInOut.query.get(id)
    if not in_out:
        return jsonify({"error": "Record not found"}), 404

    db.session.delete(in_out)
    db.session.commit()
    return jsonify({"message": "Material in/out record deleted successfully"}), 200


# ---------------- 库存查询 ----------------

# 获取当前库存
@bp_material.route('/inventory', methods=['GET'])
def get_inventory():
    # 查询 material_in_out 表中的入库和出库数据
    in_records = db.session.query(MaterialInOut).filter(MaterialInOut.status == 'in').all()
    out_records = db.session.query(MaterialInOut).filter(MaterialInOut.status == 'out').all()

    # 初始化库存字典
    inventory = {}

    # 处理入库记录
    for record in in_records:
        if record.part_number in inventory:
            inventory[record.part_number]['quantity'] += record.quantity
        else:
            # 根据料号查询物料信息
            material_info = db.session.query(MaterialInfo).filter(MaterialInfo.part_number == record.part_number).first()
            inventory[record.part_number] = {
                'name': material_info.name,
                'specification': material_info.specification,
                'category': material_info.category,
                'part_number': record.part_number,
                'quantity': record.quantity,
                'image_url': material_info.image_url  # 图片 URL
            }

    # 处理出库记录
    for record in out_records:
        if record.part_number in inventory:
            inventory[record.part_number]['quantity'] -= record.quantity

    # 过滤出库存大于0的记录
    inventory = {k: v for k, v in inventory.items() if v['quantity'] > 0}

    return jsonify(inventory), 200


# 根据物料名称搜索库存
@bp_material.route('/inventory/search', methods=['GET'])
def search_inventory():
    # 从查询参数获取物料名称
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "No name provided"}), 400

    # 搜索符合名称的物料信息
    materials = MaterialInfo.query.filter(MaterialInfo.name.contains(name)).all()

    # 初始化库存字典
    inventory = {}

    # 根据物料信息构建库存字典
    for material in materials:
        part_number = material.part_number
        in_records = db.session.query(MaterialInOut).filter(MaterialInOut.part_number == part_number, MaterialInOut.status == 'in').all()
        out_records = db.session.query(MaterialInOut).filter(MaterialInOut.part_number == part_number, MaterialInOut.status == 'out').all()

        # 计算库存数量
        quantity_in = sum([record.quantity for record in in_records])
        quantity_out = sum([record.quantity for record in out_records])
        quantity = quantity_in - quantity_out

        if quantity > 0:
            inventory[part_number] = {
                'name': material.name,
                'specification': material.specification,
                'category': material.category,
                'quantity': quantity,
                'image_url': material.image_url  # 图片 URL
            }

    return jsonify(inventory), 200
