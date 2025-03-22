from meow.password import get_random_password
import string

def test_simple():
    assert 1==1

def test_simple_password():
    simple_pass = get_random_password()
    assert len(simple_pass) == 8
    assert len(get_random_password(length=4))==4


def test_special_char_password():
    password = get_random_password(special_char=True)
    assert len(password) == 8
    assert any(char in string.punctuation for char in password)