"""
Contains the core fifth interpreter functionality
"""

from typing import Tuple, Optional
from fifth.stack import Stack, StackError


class Commands:
    DUPLICATE = 'DUP'
    SWAP = 'SWAP'
    PUSH = 'PUSH'
    POP = 'POP'
    ADD = '+'
    SUBTRACT = '-'
    DIVIDE = '/'
    MULTIPLY = '*'


class CommandError(Exception):
    pass


class FifthInterpreter:
    def __init__(self):
        self.stack = Stack()

    def start(self):
        """
        Begins repl session
        """
        while True:
            print(f'Stack is {self.stack}')
            _input = input()
            try:
                self.execute(_input)
            except StackError as e:
                print(f'Error: {str(e)}')
            except CommandError:
                print('Invalid command - try again')

    def execute(self, _input):
        """
        Execute command on stack
        """
        command, value = self._parse_user_input(_input)
        
        if command == Commands.ADD:
            self.stack.add()
        elif command == Commands.SUBTRACT:
            self.stack.subtract()
        elif command == Commands.DIVIDE:
            self.stack.divide()
        elif command == Commands.MULTIPLY:
            self.stack.multiply()
        elif command == Commands.DUPLICATE:
            self.stack.duplicate()
        elif command == Commands.POP:
            self.stack.pop()
        elif command == Commands.PUSH:
            if value is None:
                raise CommandError()
            self.stack.push(value)
        elif command == Commands.SWAP:
            self.stack.swap()
        else:
            raise CommandError()

    @staticmethod
    def _parse_user_input(user_input: str) -> Tuple[str, Optional[int]]:
        words = user_input.split(' ')
        if len(words) > 2:
            raise CommandError()
        elif len(words) == 2:
            command, value = words
            if not command == Commands.PUSH:
                raise CommandError()
            try:
                value = int(value)
            except ValueError:
                raise CommandError()
        else:
            command = words[0]
            value = None

        return command, value
