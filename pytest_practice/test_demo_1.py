# import pytest


def test_1():
    print("hi")


def test_sample():
    str = "testing"
    sentence = "automation testing"
    assert str in sentence


def test_3():
    name = "python"
    str = "Python language"
    assert name in str, "name is not present in string"
