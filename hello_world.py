import os

def hello_hello():
    env = os.getenv("ENV")
    print(f'Hello, {env} environment!')

    return env

def not_covered_by_unittests():
    print("i am not covered")
    print("uncovered new code")
    return os.getenv("ENV")

def another_uncovered_func():
    not_covered_by_unittests()
    return os.getenv("ENV")

def another_one():
    print("porra")
