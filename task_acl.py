import functools

def require_role(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_data = kwargs.get('user')
            if not user_data or user_data.get('role') != required_role:
                return f"Доступ запрещен. Требуется роль: {required_role}"
            return func(*args, **kwargs)
        return wrapper
    return decorator

users = {
    'alice': {'role': 'admin'},
    'bob': {'role': 'user'},
    'eve': {'role': 'guest'}
}

current_user = 'bob'

@require_role('admin')
def delete_database(db_name, user=None):
    return f"База {db_name} удалена!"

if __name__ == "__main__":
    result = delete_database('test_db', user=users[current_user])
    print(result)