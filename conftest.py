import pytest


@pytest.fixture()
def set_up():
    print("Start tests")
    yield
    print("Finish tests")


@pytest.fixture(scope="module")
def set_group():
    print("Starting to test")
    yield
    print("Finished testing")
