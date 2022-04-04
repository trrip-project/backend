from tripp_travel import __version__
from tripp_travel import login

def test_greeting():
    assert login.sayWelcome("Venkatesh") == "Hello Venkatesh"
def test_version():
    assert __version__ == '0.1.0'
def test_mul():
    assert login.mul(2) == 4
