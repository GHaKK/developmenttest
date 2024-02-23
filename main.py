#!/usr/bin/env python
'''
Return string to main
'''
import sys


def main():
    '''
    Doc-string to pass the lint
    '''

    try:
        toprint = sys.argv[1]
    except IndexError:
        toprint=None
    print(hello_print(toprint))


def hello_print(text_to_print=None):
    '''
    Return a value
    '''
    return text_to_print


if __name__ == "__main__":
    main()
