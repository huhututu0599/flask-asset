from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     name = db.Column(db.String(50), unique=True, nullable=False, comment='用户名')
#     email = db.Column(db.String(120), unique=True, nullable=False, comment='用户邮箱')
#     password = db.Column(db.String(200), nullable=False, comment='用户密码')
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, comment='角色ID')
#
# class Asset(db.Model):
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     name = db.Column(db.String(50), nullable=False, comment='资产名称')
#     value = db.Column(db.Float, nullable=False, comment='资产价值')
#     barcode = db.Column(db.String(32), nullable=False, comment='条形码')
#     owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='所有者ID')
#     owner = db.relationship('User', backref=db.backref('assets', lazy=True))
#
# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     name = db.Column(db.String(50), unique=True, nullable=False, comment='角色名称')
#     users = db.relationship('User', backref='role', lazy=True)
#
# class Permission(db.Model):
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     name = db.Column(db.String(50), unique=True, nullable=False, comment='权限名称')
#     required_role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, comment='所需角色ID')
#     role = db.relationship('Role', backref=db.backref('permissions', lazy=True))
#
# class Measurement(db.Model):
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     measurement_value = db.Column(db.Float, nullable=False, comment='测量值')
#     display_start = db.Column(db.Float, nullable=False, comment='显示起点')
#     display_end = db.Column(db.Float, nullable=False, comment='显示终点')
#     filter_time_constant = db.Column(db.Float, nullable=False, comment='滤波器时间常数')
#     temperature_unit = db.Column(db.String(10), nullable=False, comment='温度单位')
#
# class DeviceInfo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     device_name = db.Column(db.String(100), nullable=False, comment='设备名称')
#     device_model = db.Column(db.String(100), nullable=False, comment='设备型号')
#     device_parameter = db.Column(db.String(100), nullable=False, comment='设备参数')
#     parameter_value = db.Column(db.Float, nullable=False, comment='设备参数值')
#     parameter_description = db.Column(db.String(200), nullable=True, comment='参数描述')
#     current_parameter_value = db.Column(db.Float, nullable=False, comment='当前参数值')
#     modification_time = db.Column(db.DateTime, nullable=False, comment='修改时间')
#     modified_by = db.Column(db.String(50), nullable=False, comment='修改人员')
#     modification_reason = db.Column(db.String(200), nullable=True, comment='修改原因')
#     device_photo = db.Column(db.String(255), nullable=True, comment='设备照片路径')
#     parameter_photo = db.Column(db.String(255), nullable=True, comment='设备参数照片路径')
#
#
# class TemperatureHumidity(db.Model):
#     __tablename__ = 'temperature_humidity'
#
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
#     original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
#     timestamp = db.Column(db.DateTime, default=datetime.now(), nullable=False, comment='时间')
#     temperature = db.Column(db.Float, nullable=False, comment='温度')
#     humidity = db.Column(db.Float, nullable=False, comment='湿度')
#
# class SHT40(db.Model):
#     __tablename__ = 'sht40'  # 表名
#
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
#     original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
#     timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
#     temperature = db.Column(db.Float, nullable=False, comment='温度')
#     humidity = db.Column(db.Float, nullable=False, comment='湿度')
#
# class SHT30(db.Model):
#     __tablename__ = 'sht30'  # 表名
#
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
#     original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
#     timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
#     temperature = db.Column(db.Float, nullable=False, comment='温度')
#     humidity = db.Column(db.Float, nullable=False, comment='湿度')
#
# class FSTSensor(db.Model):
#     __tablename__ = 'fst_sensor'  # 表名
#
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
#     original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
#     timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
#     temperature = db.Column(db.Float, nullable=False, comment='温度')
#
# class SGP30(db.Model):
#     __tablename__ = 'sgp30'  # 表名
#
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
#     original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
#     timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
#     co2 = db.Column(db.Float, nullable=False, comment='二氧化碳浓度')
#     tvoc = db.Column(db.Float, nullable=False, comment='总挥发性有机化合物浓度')
#
# class BME680(db.Model):
#     __tablename__ = 'bme680'  # 表名
#
#     id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
#     device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
#     original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
#     timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
#     temperature = db.Column(db.Float, nullable=False, comment='温度')
#     humidity = db.Column(db.Float, nullable=False, comment='湿度')
#     pressure = db.Column(db.Float, nullable=False, comment='压力')



class User(db.Model):
    __tablename__ = 'user'  # 用户表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    name = db.Column(db.String(50), unique=True, nullable=False, comment='用户名')
    email = db.Column(db.String(120), unique=True, nullable=False, comment='用户邮箱')
    password = db.Column(db.String(200), nullable=False, comment='用户密码')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, comment='角色ID')

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    name = db.Column(db.String(50), nullable=False, comment='资产名称')
    value = db.Column(db.Float, nullable=False, comment='资产价值')
    barcode = db.Column(db.String(32), nullable=False, comment='条形码')
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='所有者ID')
    owner = db.relationship('User', backref=db.backref('assets', lazy=True))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    name = db.Column(db.String(50), unique=True, nullable=False, comment='角色名称')
    users = db.relationship('User', backref='role', lazy=True)

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    name = db.Column(db.String(50), unique=True, nullable=False, comment='权限名称')
    required_role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, comment='所需角色ID')
    role = db.relationship('Role', backref=db.backref('permissions', lazy=True))

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    measurement_value = db.Column(db.Float, nullable=False, comment='测量值')
    display_start = db.Column(db.Float, nullable=False, comment='显示起点')
    display_end = db.Column(db.Float, nullable=False, comment='显示终点')
    filter_time_constant = db.Column(db.Float, nullable=False, comment='滤波器时间常数')
    temperature_unit = db.Column(db.String(10), nullable=False, comment='温度单位')

class DeviceInfo(db.Model):
    __tablename__ = 'dev_device_info'  # 设备信息表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_name = db.Column(db.String(100), nullable=False, comment='设备名称')
    device_model = db.Column(db.String(100), nullable=False, comment='设备型号')
    device_parameter = db.Column(db.String(100), nullable=False, comment='设备参数')
    parameter_value = db.Column(db.Float, nullable=False, comment='设备参数值')
    parameter_description = db.Column(db.String(200), nullable=True, comment='参数描述')
    current_parameter_value = db.Column(db.Float, nullable=False, comment='当前参数值')
    modification_time = db.Column(db.DateTime, nullable=False, comment='修改时间')
    modified_by = db.Column(db.String(50), nullable=False, comment='修改人员')
    modification_reason = db.Column(db.String(200), nullable=True, comment='修改原因')
    device_photo = db.Column(db.String(255), nullable=True, comment='设备照片路径')
    parameter_photo = db.Column(db.String(255), nullable=True, comment='设备参数照片路径')

class TemperatureHumidity(db.Model):
    __tablename__ = 'dev_temperature_humidity'  # 温湿度表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
    original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
    temperature = db.Column(db.Float, nullable=False, comment='温度')
    humidity = db.Column(db.Float, nullable=False, comment='湿度')

class SHT40(db.Model):
    __tablename__ = 'dev_sht40'  # SHT40 设备表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
    original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
    temperature = db.Column(db.Float, nullable=False, comment='温度')
    humidity = db.Column(db.Float, nullable=False, comment='湿度')

class SHT30(db.Model):
    __tablename__ = 'dev_sht30'  # SHT30 设备表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
    original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
    temperature = db.Column(db.Float, nullable=False, comment='温度')
    humidity = db.Column(db.Float, nullable=False, comment='湿度')

class FSTSensor(db.Model):
    __tablename__ = 'dev_fst_sensor'  # FST 设备表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
    original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
    temperature = db.Column(db.Float, nullable=False, comment='温度')

class SGP30(db.Model):
    __tablename__ = 'dev_sgp30'  # SGP30 设备表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
    original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
    co2 = db.Column(db.Float, nullable=False, comment='二氧化碳浓度')
    tvoc = db.Column(db.Float, nullable=False, comment='总挥发性有机化合物浓度')

class BME680(db.Model):
    __tablename__ = 'dev_bme680'  # BME680 设备表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
    original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
    temperature = db.Column(db.Float, nullable=False, comment='温度')
    humidity = db.Column(db.Float, nullable=False, comment='湿度')
    pressure = db.Column(db.Float, nullable=False, comment='压力')
    gas_resistance = db.Column(db.Float, nullable=False, comment='GAS')

class LTR329(db.Model):
    __tablename__ = 'dev_ltr329'  # BME680 设备表
    id = db.Column(db.Integer, primary_key=True, comment='唯一标识符')
    device_id = db.Column(db.String(50), nullable=False, comment='设备ID')
    original_id = db.Column(db.String(50), nullable=False, comment='原始ID')
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='时间')
    lux = db.Column(db.Float, nullable=False, comment='光照强度')
    ir = db.Column(db.Float, nullable=False, comment='红外光强度')


# Model for storing material information
class MaterialInfo(db.Model):
    __tablename__ = 'material_info'
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    part_number = db.Column(db.String(100), unique=True, nullable=False, comment='料号')  # 料号
    name = db.Column(db.String(100), nullable=False, comment='名称')  # 名称
    specification = db.Column(db.String(100), nullable=False, comment='规格')  # 规格
    category = db.Column(db.String(50), nullable=True, comment='类别')  # 类别
    image_url = db.Column(db.String(250), nullable=True, comment='图片链接')  # 类别

# Model for tracking material in/out movements
class MaterialInOut(db.Model):
    __tablename__ = 'material_in_out'
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    status = db.Column(db.String(10), nullable=False, comment='出入库状态 (in/out)')  # "in" or "out"
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, comment='出入库时间')  # 出入库时间
    part_number = db.Column(db.String(100), db.ForeignKey('material_info.part_number'), nullable=False, comment='料号')  # 料号
    quantity = db.Column(db.Integer, nullable=False, comment='数量')  # 数量
    price = db.Column(db.Float, nullable=False, comment='单价')  # 单价