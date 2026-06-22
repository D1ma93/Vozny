import functools
from datetime import datetime

def log_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = (
            f"[{timestamp}] Функция: {func.__name__} | "
            f"Аргументы: args={args}, kwargs={kwargs} | "
            f"Результат: {result}\n"
        )
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(log_line)
        return result
    return wrapper

@log_args
def calc_power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    calc_power(2, 10)
    calc_power(5, exponent=3)