"""
Contains a Stack datastructure which contains run time state
"""

from typing import List


NOT_ENOUGH_ELEMENTS_ERROR_MSG = 'Stack requires {} elements to carry out this operation'
ZERO_DIVISION_ERROR_MSG = 'Cannot divide by zero'


class StackError(Exception):
    pass


class Stack:
    def __init__(self, state: List[int] = []):
        """
        Initialise the stack with an optional starting state
        """
        self._data = state

    def __repr__(self):
        return str(self._data)

    def __eq__(self, other: List[int]):
        return self._data == other

    def push(self, value: int):
        """
        Add value to the top of the stack
        """
        self._data.append(value)

    def pop(self):
        """
        Remove the top element of the stack
        """
        self._data = self._data[:-1]

    def swap(self):
        """
        Swap the top two elements of the stack
        """
        self._check_stack_size()
        self._data = self._data[:-2] + [self._data[-1], self._data[-2]]

    def duplicate(self):
        """
        Duplicate the top element of the stack
        """
        self._data.append(self._data[-1])

    def add(self):
        """
        Replace top two elements in stack (s) with the result of s[-1] + [s-2]
        e.g. [1, 2, 2] -> [1, 4]
        """
        self._check_stack_size()
        self._data = self._data[:-2] + [self._data[-2] + self._data[-1]]

    def subtract(self):
        """
        Replace top two elements in stack (s) with the result of s[-2] - s[-1]
        e.g. [1, 2, 2] -> [1, 0]
        """
        self._check_stack_size()
        self._data = self._data[:-2] + [self._data[-2] - self._data[-1]]

    def multiply(self):
        """
        Replace top two elements in stack (s) with the result of s[-2] * s[-1]
        e.g. [1, 2, 2] -> [1, 0]
        """
        self._check_stack_size()
        self._data = self._data[:-2] + [self._data[-2] * self._data[-1]]

    def divide(self):
        """
        Replace top two elements in stack (s) with the result of s[-2] / s[-1]
        e.g. [1, 2, 2] -> [1, 0]
        """
        self._check_stack_size()
        if self._data[-1] == 0:
            raise StackError(ZERO_DIVISION_ERROR_MSG)
        replacement = self._data[-2] // self._data[-1]
        self._data = self._data[:-2] + [replacement]

    def _check_stack_size(self, num_elements_required: int = 2):
        """
        Many stack operations require the stack to contain a minimum number of
        2 elements.
        """
        if len(self._data) < num_elements_required:
            raise StackError(
                NOT_ENOUGH_ELEMENTS_ERROR_MSG.format(num_elements_required)
            )
