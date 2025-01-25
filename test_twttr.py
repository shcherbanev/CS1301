#!/bin/env python
import pytest
from twttr import shorten


def test_twttr():
    assert shorten("test") == str("tst")
    assert shorten("tAst") == str("tst")
    assert shorten("t1st") == str("t1st")
    assert shorten("t.st") == str("t.st")


"""
def main():

    mess = input("What's your message??: ")
    print(shorten(mess))
"""
if __name__ == "__main__":
    main()
