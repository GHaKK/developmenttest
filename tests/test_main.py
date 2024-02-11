from main import hello_print

def test_toprint_string():
# Direct string test
    hello_print("Hello World") == "Hello World"


def test_toprint_variable():
# Variable test
    string_to_print = "Hello World"
    hello_print(string_to_print) == "Hello World"

def test_toprint_int():
# Integer test
    hello_print(1) == int(1)

def test_toprint_empty():
    hello_print() == None
