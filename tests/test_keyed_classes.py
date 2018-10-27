import pytest

from keyed_classes import __version__
from keyed_classes import KeyedClass
from keyed_classes import KeyedClassMeta


def test_version():
    assert __version__ == '0.1.0'


def test_same_key_same_object():
    class LocalClass(KeyedClass):
        def __init__(self, key):
            pass

    instance_one = LocalClass('test_same_key_same_object')
    instance_two = LocalClass('test_same_key_same_object')
    assert instance_one is instance_two

def test_same_key_same_object_meta():
    class LocalClass(metaclass=KeyedClassMeta):
        def __init__(self, key):
            pass

    instance_one = LocalClass('test_same_key_same_object')
    instance_two = LocalClass('test_same_key_same_object')
    assert instance_one is instance_two

def test_different_classes_can_have_same_key():
    class LocalClass(KeyedClass):
        def __init__(self, key):
            pass

    class LocalClass2(KeyedClass):
        def __init__(self, key):
            pass

    instance_one = LocalClass('test_different_classes_can_have_same_key')
    instance_two = LocalClass2('test_different_classes_can_have_same_key')
    assert instance_one is not instance_two

def test_different_classes_can_have_same_key_meta():
    class LocalClass(metaclass=KeyedClassMeta):
        def __init__(self, key):
            pass

    class LocalClass2(metaclass=KeyedClassMeta):
        def __init__(self, key):
            pass

    instance_one = LocalClass('test_different_classes_can_have_same_key')
    instance_two = LocalClass2('test_different_classes_can_have_same_key')
    assert instance_one is not instance_two

