from flask import Blueprint, request, jsonify
from models import db, LTR329
from datetime import datetime, timedelta

bp_ltr329 = Blueprint('ltr329', __name__)

@bp_ltr329.route('/ltr329', methods=['POST'])
def receive_ltr329_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if isinstance(data, list):
        records = []
        for item in data:
            device_id = item.get('device_id')
            original_id = item.get('original_id')
            lux = item.get('lux')
            ir = item.get('ir')

            if not all([device_id, original_id, lux, ir]):
                return jsonify({"error": "Missing required fields"}), 400

            timestamp = datetime.utcnow() + timedelta(hours=8)

            new_record = LTR329(
                device_id=device_id,
                original_id=original_id,
                timestamp=timestamp,
                lux=lux,
                ir=ir
            )

            records.append(new_record)

        db.session.add_all(records)
        db.session.commit()
        return jsonify({"message": "Data received successfully"}), 201

    else:
        device_id = data.get('device_id')
        original_id = data.get('original_id')
        lux = data.get('lux')
        ir = data.get('ir')

        if not all([device_id, original_id, lux, ir]):
            return jsonify({"error": "Missing required fields"}), 400

        timestamp = datetime.utcnow() + timedelta(hours=8)

        new_record = LTR329(
            device_id=device_id,
            original_id=original_id,
            timestamp=timestamp,
            lux=lux,
            ir=ir
        )

        db.session.add(new_record)
        db.session.commit()
        return jsonify({"message": "Data received successfully"}), 201


@bp_ltr329.route('/ltr329/device_ids', methods=['GET'])
def get_device_ids():
    # 获取所有唯一的设备ID
    device_ids = db.session.query(LTR329.device_id).distinct().all()

    # 提取设备ID并构建返回数据
    unique_device_ids = [device_id[0] for device_id in device_ids]

    return jsonify(unique_device_ids), 200

#
# @bp_ltr329.route('/ltr329/data/<device_id>', methods=['GET'])
# def get_data_by_device_id(device_id):
#     start_time = request.args.get('start_time')
#     end_time = request.args.get('end_time')
#
#     # 查询指定 device_id 的所有数据
#     query = db.session.query(LTR329).filter_by(device_id=device_id)
#
#     # 如果提供了时间范围，则按时间范围过滤
#     if start_time:
#         try:
#             start_time = datetime.fromisoformat(start_time)  # 使用 ISO 格式
#             query = query.filter(LTR329.timestamp >= start_time)
#         except ValueError:
#             return jsonify({"error": "Invalid start_time format. Use YYYY-MM-DDTHH:MM"}), 400
#
#     if end_time:
#         try:
#             end_time = datetime.fromisoformat(end_time)  # 使用 ISO 格式
#             query = query.filter(LTR329.timestamp <= end_time)
#         except ValueError:
#             return jsonify({"error": "Invalid end_time format. Use YYYY-MM-DDTHH:MM"}), 400
#
#     # 获取查询结果
#     data_records = query.all()
#
#     # 将数据转换为字典格式
#     data_list = [
#         {
#             "id": record.id,
#             "device_id": record.device_id,
#             "original_id": record.original_id,
#             "timestamp": record.timestamp.isoformat(),  # Convert datetime to ISO format
#             "lux": record.lux,
#             "ir": record.ir
#         }
#         for record in data_records
#     ]
#
#     if not data_list:
#         return jsonify({"message": "No data found for the specified device_id."}), 404
#
#     return jsonify(data_list), 200
@bp_ltr329.route('/ltr329/data/<device_id>', methods=['GET'])
def get_data_by_device_id(device_id):
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    # 查询指定 device_id 的所有数据
    query = db.session.query(LTR329).filter_by(device_id=device_id)

    # 如果提供了时间范围，则按时间范围过滤
    if start_time:
        try:
            start_time = datetime.fromisoformat(start_time)
            query = query.filter(LTR329.timestamp >= start_time)
        except ValueError:
            return jsonify({"error": "Invalid start_time format. Use YYYY-MM-DDTHH:MM"}), 400

    if end_time:
        try:
            end_time = datetime.fromisoformat(end_time)
            query = query.filter(LTR329.timestamp <= end_time)
        except ValueError:
            return jsonify({"error": "Invalid end_time format. Use YYYY-MM-DDTHH:MM"}), 400

    # 实现分页
    paginated_data = query.paginate(page=page, per_page=per_page, error_out=False)
    data_list = [
        {
            "id": record.id,
            "device_id": record.device_id,
            "original_id": record.original_id,
            "timestamp": record.timestamp.isoformat(),
            "lux": record.lux,
            "ir": record.ir
        }
        for record in paginated_data.items
    ]

    response = {
        "data": data_list,
        "page": page,
        "per_page": per_page,
        "total_pages": paginated_data.pages,
        "total_items": paginated_data.total
    }

    if not data_list:
        return jsonify({"message": "No data found for the specified device_id."}), 404

    return jsonify(response), 200
