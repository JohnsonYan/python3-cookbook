#!/usr/bin/env python
# encoding: utf-8

class Bar_1:
    def __call__(self, *args, **kwargs):
        print('i am instance method')


b = Bar_1()  # 实例化
b()  # 实例对象b 可以作为函数调用 等同于b.__call__ 使用


# OUT: i am instance method


# 带参数的类装饰器
class Bar:

    def __init__(self, p1):
        self.p1 = p1

    def __call__(self, func):
        def wrapper():
            print("Starting", func.__name__)
            print("p1=", self.p1)
            func()
            print("Ending", func.__name__)
        return wrapper


@Bar("foo bar")
def hello():
    print("Hello")

# 上面的语法糖写法 等价于 hello = Bar('foo bar')(hello)


if __name__ == "__main__":
    hello()
