import pytest
import sys


@pytest.mark.parametrize("user_name, password",
                         [("admin", "admin"),
                          ("mir", "new123"),
                          ("ayan", "test4321")])
def test_login(user_name, password):
    print(user_name)
    print(password)
