import pytest


@pytest.fixture()
def setup():
    print("start...")
    yield
    print("end...")


def test_one(setup):
    print("test 1")


def test_two(setup):
    print("test 2")


def test_three(setup):
    print("test 3")
