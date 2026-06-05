import numpy as np


def calculate_mean(data: list[float]) -> float:
    """计算平均值"""
    return np.mean(data)


# 测试
numbers = [1, 2, 3, 4, 5]
result = calculate_mean(numbers)
print(f"平均值: {result}")

# 故意写错，看看有没有错误提示
prnt("hello")
result
