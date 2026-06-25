"""一个简单的计算器模块，用于演示 pytest 的基本用法。"""


def add(a, b):
    """返回两个数之和。"""
    return a + b


def subtract(a, b):
    """返回 a 减 b 的结果。"""
    return a - b


def multiply(a, b):
    """返回两个数之积。"""
    return a * b


def divide(a, b):
    """返回 a 除以 b 的结果。除数为 0 时抛出 ValueError。"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def is_even(n):
    """判断一个整数是否为偶数。"""
    return n % 2 == 0
