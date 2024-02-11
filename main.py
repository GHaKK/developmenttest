#!/usr/bin/env python

def main():
    toprint = "Hello World"
    try:
        print(hello_print(toprint))
    except Exception as e:
        print(e)
def hello_print(text_to_print = None):
    return (text_to_print)

if __name__ == "__main__":
    main()
