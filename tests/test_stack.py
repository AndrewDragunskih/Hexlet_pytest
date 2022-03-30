import pytest

def test_stack1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
