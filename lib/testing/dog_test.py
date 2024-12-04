from dog import Dog
import io
import sys

def test_name_not_empty():
    '''prints "Name must be string between 1 and 25 characters." if empty string.'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    Dog(name="", breed="Labrador")
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n"
