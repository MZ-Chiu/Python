#!/usr/bin/python
# -*- coding: utf-8 -*-

print("# 类和实例")


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


print("# 访问限制")


class Human(object):
    def __init__(self, name, len):
        self.__name = name
        self.__len = len

    def print_len(self):
        print('%s: %s' % (self.__name, self.__len))



print("# 继承和多态")


