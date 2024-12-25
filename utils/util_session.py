from flask import session

def get_user_role_id():
    role_id = session.get('role_id')
    if role_id is None:
        # 处理没有角色 ID 的情况，例如返回 0 或引发异常
        raise ValueError("Role ID is not set in session")
    return role_id
