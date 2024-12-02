import pytest

@pytest.fixture()
def before_after():
    print('Before test')
    yield #---место для теста
    print('\nAfter test') #---с переносом строки

def test_demo1(before_after):
    assert 1 == 1

def test_demo2():
    assert 2 == 2


