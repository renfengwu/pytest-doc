"""calculator 模块的 pytest 测试用例。

演示要点：
1. 基本断言            -> test_add / test_subtract / test_multiply
2. 异常断言            -> test_divide_by_zero
3. 参数化（一组数据跑多次） -> test_is_even
4. fixture（共享前置数据） -> calc_data
"""

import pytest
from src.calculator import add, divide, is_even, multiply, subtract


# ---------- 1. 基本断言 ----------
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


# ---------- 2. 异常断言 ----------
def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    # 期望抛出 ValueError，并校验错误信息
    with pytest.raises(ValueError, match="除数不能为 0"):
        divide(1, 0)


# ---------- 3. 参数化 ----------
@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (7, False),
    ],
)
def test_is_even(number, expected):
    assert is_even(number) == expected


# ---------- 4. fixture ----------
@pytest.fixture
def calc_data():
    """提供一组共享的测试数据。"""
    return {"a": 8, "b": 2}


def test_with_fixture(calc_data):
    assert add(calc_data["a"], calc_data["b"]) == 10
    assert divide(calc_data["a"], calc_data["b"]) == 4
