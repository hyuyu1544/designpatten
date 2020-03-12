"""Used 4 differents way to implement singleton.

1.decorator
2.class
3.__new__
4.metaclass
"""
from singleton import (
    singleton,
    Singleton,
    Single,
    SINGLE
)


@singleton
class demo1:
    def __init__(self):
        pass


@Singleton
class demo2:
    def __init__(self):
        pass


class demo3(Single):
    def __init__(self):
        pass


class demo4(metaclass=SINGLE):
    def __init__(self):
        pass


if __name__ == "__main__":
    print('Method 1: decorator')
    cl1 = demo1()
    cl2 = demo1()
    print(id(cl1) == id(cl2))
    print('Method 2: class')
    cl1 = demo2()
    cl2 = demo2()
    print(id(cl1) == id(cl2))
    print('Method 3: __new__')
    cl1 = demo3()
    cl2 = demo3()
    print(id(cl1) == id(cl2))
    print('Method 4: metaclass')
    cl1 = demo4()
    cl2 = demo4()
    print(id(cl1) == id(cl2))
