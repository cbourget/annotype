import pytest

from annotype import annotyped
from marshmallow import (
    Schema,
    fields
)


class SchemaForB(Schema):
    ba = fields.Str()
    bb = fields.Int(required=True)


@annotyped(load=True)
def foo(a: fields.Str(), b: SchemaForB, c: fields.Str() = None):
    return (a, b, c)


@annotyped()
def bar(a):
    return a


def test_invalid_arguments():
    # a should be a string but is an integer
    with pytest.raises(TypeError) as exc_info:
        foo(1, {'ba': 'world', 'bb': 1})

    # b should be a dict with the key 'bb'
    with pytest.raises(TypeError) as exc_info:
        foo('hello', {'ba': 'world'})

    # c is a keyword argument and should be a string
    with pytest.raises(TypeError) as exc_info:
        foo('hello', {'ba': 'world', 'bb': 1}, c=1)


def test_valid_arguments():
    # all arguments are valid
    assert foo('hello', {'ba': 'world', 'bb': 1}) == (
        'hello',
        {'ba': 'world', 'bb': 1},
        None
    )

    # b.bb is a string but marshmallow formats automatically it to an integer
    assert foo('hello', {'ba': 'world', 'bb': '1'}) == (
        'hello',
        {'ba': 'world', 'bb': 1},
        None
    )

    # all arguments are passed as keyword arguments
    assert foo(b={'ba': 'world', 'bb': '1'}, c='1', a='hello') == (
        'hello',
        {'ba': 'world', 'bb': 1},
        '1'
    )

    # function as no annotation
    assert bar('hello') == 'hello'
