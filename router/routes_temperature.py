# router/routes_temperature.py

from flask import Blueprint, request, jsonify
from models import db, TemperatureHumidity
from datetime import datetime, timedelta

bp_temperature = Blueprint('temperature', __name__)

@bp_temperature.route('/temperature', methods=['POST'])
def receive_temperature_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # 从请求中提取数据
    device_id = data.get('device_id')
    original_id = data.get('original_id')
    temperature = data.get('temperature')
    humidity = data.get('humidity')

    # 检查必要的字段
    if not all([device_id, original_id, temperature, humidity]):
        return jsonify({"error": "Missing required fields"}), 400

    # 获取当前 UTC 时间并转换为北京时间
    timestamp = datetime.utcnow() + timedelta(hours=8)

    # 创建新的温湿度记录
    new_record = TemperatureHumidity(
        device_id=device_id,
        original_id=original_id,
        timestamp=timestamp,  # 使用转换后的时间
        temperature=temperature,
        humidity=humidity
    )

    db.session.add(new_record)
    db.session.commit()

    return jsonify({"message": "Data received successfully"}), 201

# 查询温湿度数据接口
@bp_temperature.route('/temperature', methods=['GET'])
def get_temperature_data():
    device_id = request.args.get('device_id')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    # 构建查询
    query = TemperatureHumidity.query

    # 如果提供了设备ID，则按设备ID过滤
    if device_id:
        query = query.filter(TemperatureHumidity.device_id == device_id)

    # 如果提供了时间范围，则按时间范围过滤
    if start_time:
        try:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            query = query.filter(TemperatureHumidity.timestamp >= start_time)
        except ValueError:
            return jsonify({"error": "Invalid start_time format. Use YYYY-MM-DD HH:MM:SS"}), 400

    if end_time:
        try:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
            query = query.filter(TemperatureHumidity.timestamp <= end_time)
        except ValueError:
            return jsonify({"error": "Invalid end_time format. Use YYYY-MM-DD HH:MM:SS"}), 400

    # 获取查询结果
    results = query.order_by(TemperatureHumidity.timestamp.asc()).all()

    # 构建返回数据
    data = [
        {
            "id": record.id,
            "device_id": record.device_id,
            "original_id": record.original_id,
            "timestamp": record.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            "temperature": record.temperature,
            "humidity": record.humidity,
        }
        for record in results
    ]

    return jsonify(data), 200


# 新增查询设备ID接口
@bp_temperature.route('/temperature_deviceid', methods=['GET'])
def get_device_ids():
    # 获取所有唯一的设备ID
    device_ids = db.session.query(TemperatureHumidity.device_id).distinct().all()

    # 提取设备ID并构建返回数据
    unique_device_ids = [device_id[0] for device_id in device_ids]

    return jsonify(unique_device_ids), 200