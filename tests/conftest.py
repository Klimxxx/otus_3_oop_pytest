import pytest

@pytest.fixture(scope="session", autouse=True)
def start_info():
    print('/nTest started')
    yield
    print('/nTest finish')




