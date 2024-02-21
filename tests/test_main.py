'''
TESTING!!!
'''
from main import hello_print


def test_toprint_string():
    '''
    Direct string test
    '''
    assert hello_print("Hello World") == "Hello World"


def test_toprint_variable():
    '''
    Variable test
    '''
    string_to_print = "Hello World"
    assert hello_print(string_to_print) == "Hello World"


def test_toprint_int():
    '''
    Integer test
    '''
    assert hello_print(1) == int(1)


def test_toprint_empty():
    '''
    Empty string test
    '''
    assert hello_print() is None
