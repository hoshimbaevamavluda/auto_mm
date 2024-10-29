import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish")


@pytest.fixture(scope="module")
# 1 раз до начала/конца теста идет энтер систем и в конце
def set_group():
    print("Enter system")
    yield
    print("Exit system")