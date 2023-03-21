import pytest

@pytest.fixture(scope="session")
def my_setup(request):
    print('\nDoing setup')
    def fin():
        print ("\nDoing teardown")
    request.addfinalizer(fin)