#!/usr/bin/env python
import sys


def main():
    if len(sys.argv) < 2:
        toprint = "No printing"
    else:
        toprint = sys.argv[1]
    try:
        print(hello_print(toprint))
    except Exception as e:
        print(e)


def hello_print(text_to_print=None):
    return (text_to_print)


if __name__ == "__main__":
    main()
