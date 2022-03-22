"""
Tests for the FifthInterpreter class
"""

from unittest.mock import Mock

import pytest

from fifth.fifth_interpreter import (
    FifthInterpreter,
    CommandError
)


@pytest.fixture
def fifth():
    fifth = FifthInterpreter()
    fifth.stack = Mock()
    return fifth


def test_execute_swap(fifth):
    fifth.execute('SWAP')
    fifth.stack.swap.assert_called_once_with()


def test_execute_dup(fifth):
    fifth.execute('DUP')
    fifth.stack.duplicate.assert_called_once_with()


def test_execute_pop(fifth):
    fifth.execute('POP')
    fifth.stack.pop.assert_called_once_with()


def test_execute_push(fifth):
    fifth.execute('PUSH 5')
    fifth.stack.push.assert_called_once_with(5)


def test_execute_add(fifth):
    fifth.execute('+')
    fifth.stack.add.assert_called_once_with()


def test_execute_subtract(fifth):
    fifth.execute('-')
    fifth.stack.subtract.assert_called_once_with()


def test_execute_multiply(fifth):
    fifth.execute('*')
    fifth.stack.multiply.assert_called_once_with()


def test_execute_divide(fifth):
    fifth.execute('/')
    fifth.stack.divide.assert_called_once_with()


def test_invalid_command_too_many_words(fifth):
    with pytest.raises(CommandError):
        fifth.execute('PUSH 5 5')


def test_invalid_command_push_non_int(fifth):
    with pytest.raises(CommandError):
        fifth.execute('PUSH FIVE')


def test_invalid_command_push_no_value(fifth):
    with pytest.raises(CommandError):
        fifth.execute('PUSH')


def test_invalid_command_not_recognised(fifth):
    with pytest.raises(CommandError):
        fifth.execute('SQUARE')
