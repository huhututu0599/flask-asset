from werkzeug.security import generate_password_hash, check_password_hash

# 用户注册时
def create_user(password):
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    # 假设这里是将 hashed_password 存储到数据库的过程
    return hashed_password

# 用户登录时
def verify_user(stored_hashed_password, input_password):
    return check_password_hash(stored_hashed_password, input_password)

# 示例
if __name__ == "__main__":
    password = "admin"
    stored_hashed_password = create_user(password)
    print(f"Stored Hashed Password: {stored_hashed_password}")

    # 验证密码
    is_password_correct = verify_user(stored_hashed_password, "admin")
    print(f"Password Verification (correct): {'Success' if is_password_correct else 'Failure'}")

    is_password_incorrect = verify_user(stored_hashed_password, "wrong_password")
    print(f"Password Verification (incorrect): {'Success' if is_password_incorrect else 'Failure'}")
