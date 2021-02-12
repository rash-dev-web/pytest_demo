import pytest
import sys


@pytest.mark.skip
def test_one():
    print("test one..")


@pytest.mark.skipif(sys.version_info < (3, 9), reason="python version not supported")
def test_add_product():
    print("test one..")


@pytest.mark.xfail
def test_logout():
    print("test one..")


@pytest.mark.xpass
def test_logout():
    print("test one..")


