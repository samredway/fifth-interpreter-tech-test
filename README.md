# Fifth Interpreter Tech Test

This repository contains code written in response to the `Stack` task outlined [here](https://github.com/turner-townsend/backend-assessment#stack).

## Setup

I am using python3.9 if you don't have this installed on your system I would recommend
using pyenv to install this version - documentation [here](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv).

I recommend installing the requirements to a virtual environment using python venv. You can
see the documentation [here](https://docs.python.org/3/library/venv.html).

However, the only current dependency is `pytest`.

On mac I ran:

    python -m venv venv

Then to install the requirements:

    . ./venv/bin/pip install -r requirements.txt

When you want to activate the virtual environment you now run

    . ./venv/bin/activate
    
## Running the interpreter

From the project root activate the virtual environment and then run fifth with

    python -m fifth

Use `ctrl-c` to exit.


## Running the tests

Activate the virtual environment then run the tests using pytest

    pytest fifth/tests
