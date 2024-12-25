from flask import Blueprint, request, jsonify
from models import db, SHT30  # Make sure SHT30 is defined in your models
from datetime import datetime, timedelta

bp_sht30 = Blueprint('sht30', __name__)
@bp_sht30.route('/sht30', methods=['POST'])
def receive_sht30_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if isinstance(data, list):
        records = []
        for item in data:
            device_id = item.get('device_id')
            original_id = item.get('original_id')
            temperature = item.get('temperature')
            humidity = item.get('humidity')

            if not all([device_id, original_id, temperature, humidity]):
                return jsonify({"error": "Missing required fields"}), 400

            timestamp = datetime.utcnow() + timedelta(hours=8)

            new_record = SHT30(
                device_id=device_id,
                original_id=original_id,
                timestamp=timestamp,
                temperature=temperature,
                humidity=humidity
            )

            records.append(new_record)

        db.session.add_all(records)
        db.session.commit()
        return jsonify({"message": "Data received successfully"}), 201

    else:
        device_id = data.get('device_id')
        original_id = data.get('original_id')
        temperature = data.get('temperature')
        humidity = data.get('humidity')

        if not all([device_id, original_id, temperature, humidity]):
            return jsonify({"error": "Missing required fields"}), 400

        timestamp = datetime.utcnow() + timedelta(hours=8)

        new_record = SHT30(
            device_id=device_id,
            original_id=original_id,
            timestamp=timestamp,
            temperature=temperature,
            humidity=humidity
        )

        db.session.add(new_record)
        db.session.commit()
        return jsonify({"message": "Data received successfully"}), 201



@bp_sht30.route('/dev_sht30/device_ids', methods=['GET'])
def get_device_ids():
    # 获取所有唯一的 device_id
    device_ids = db.session.query(SHT30.device_id).distinct().all()

    # 提取 device_id 并构建返回数据
    unique_device_ids = [device_id[0] for device_id in device_ids]

    return jsonify(unique_device_ids), 200


@bp_sht30.route('/sht_30/data/<device_id>', methods=['GET'])
def get_data_by_device_id(device_id):
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    # 查询指定 device_id 的所有数据
    query = db.session.query(SHT30).filter_by(device_id=device_id)

    # 如果提供了时间范围，则按时间范围过滤
    if start_time:
        try:
            start_time = datetime.fromisoformat(start_time)
            query = query.filter(SHT30.timestamp >= start_time)
        except ValueError:
            return jsonify({"error": "Invalid start_time format. Use YYYY-MM-DDTHH:MM"}), 400

    if end_time:
        try:
            end_time = datetime.fromisoformat(end_time)
            query = query.filter(SHT30.timestamp <= end_time)
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
            "temperature": record.temperature,
            "humidity": record.humidity
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
