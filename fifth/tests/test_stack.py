""" Tests for Stack data type """

import pytest

from fifth.stack import (
    Stack,
    StackError,
    ZERO_DIVISION_ERROR_MSG,
    NOT_ENOUGH_ELEMENTS_ERROR_MSG
)


def test_push():
    stack = Stack()
    assert stack == []
    stack.push(3)
    assert stack == [3]
    stack.push(11)
    assert stack == [3, 11]


def test_pop():
    stack = Stack([1, 2])
    stack.pop()
    assert stack == [1]


def test_swap():
    stack = Stack([1, 2, 3])
    stack.swap()
    assert stack == [1, 3, 2]


def test_swap_not_enough_elements_error():
    stack = Stack([1])
    with pytest.raises(StackError) as e:
        stack.swap()
    assert str(e.value) == NOT_ENOUGH_ELEMENTS_ERROR_MSG.format(2)


def test_duplicate():
    stack = Stack([1, 2])
    stack.duplicate()
    assert stack == [1, 2, 2]


def test_add():
    stack = Stack([1, 2, 3])
    stack.add()
    assert stack == [1, 5]


def test_subtract():
    stack = Stack([1, 2, 3])
    stack.subtract()
    assert stack == [1, -1]


def test_subtract_not_enough_elements_error():
    stack = Stack([1])
    with pytest.raises(StackError) as e:
        stack.subtract()
    assert str(e.value) == NOT_ENOUGH_ELEMENTS_ERROR_MSG.format(2)


def test_multiply():
    stack = Stack([1, 2, 3])
    stack.multiply()
    assert stack == [1, 6]


def test_multiply_not_enough_elements_error():
    stack = Stack([1])
    with pytest.raises(StackError) as e:
        stack.multiply()
    assert str(e.value) == NOT_ENOUGH_ELEMENTS_ERROR_MSG.format(2)


def test_divide():
    stack = Stack([1, 4, 2])
    stack.divide()
    assert stack == [1, 2]


def test_divide_rounds_down():
    stack = Stack([1, 8, 5])
    stack.divide()
    assert stack == [1, 1]


def test_divide_by_zero():
    stack = Stack([1, 1, 0])
    with pytest.raises(StackError) as e:
        stack.divide()
    assert str(e.value) == ZERO_DIVISION_ERROR_MSG


def test_divide_not_enough_elements_error():
    stack = Stack([1])
    with pytest.raises(StackError) as e:
        stack.divide()
    assert str(e.value) == NOT_ENOUGH_ELEMENTS_ERROR_MSG.format(2)

