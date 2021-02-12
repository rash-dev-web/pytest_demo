import pytest


@pytest.mark.smoke
def test_one():
    print("test one..")


@pytest.mark.regression
def test_add_product():
    print("test one..")


@pytest.mark.smoke
def test_logout():
    print("test one..")
