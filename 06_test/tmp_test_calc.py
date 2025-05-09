import pytest
from calc import add


@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (10, 5, 15)]
)
# 加算関数 add のテスト
def test_add_param(a, b, expected):
    assert add(a, b) == expected


# bが0の場合、ValueErrorを発生させる除算関数
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# 0で除算したときにValueErrorが発生するかをテスト
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# 通常の除算が正しく行われるかをテスト
def test_divide_normal():
    result = divide(10, 2)
    assert result == 5
