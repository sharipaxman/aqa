import pytest

@pytest.fixture
def before_after():
    print('Before test')
    yield None
    print('\nAfter test')

def test_demo1(before_after):
    assert 1 == 1

