'''
TESTING!!!
'''
import sys
from main import hello_print
from main import main


def test_print_main_with_args(mocker):
    '''
    Test main with arguments
    '''
    sys.argv = ["python", "main", "hello"]
    mocker.patch("builtins.print")
    main()
    assert print.called_once_with("hello")


def test_print_main_without_args():
    '''
    Test main without arguments
    '''
    sys.argv = ["python", "main"]
    assert main() is None


def test_print_main_integer(mocker):
    '''
    Integer conversion in main
    '''
    sys.argv = ["python", "main", "1"]
    mocker.patch("builtins.print")
    main()
    assert print.called_once_with(1)


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
