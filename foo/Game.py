# -*- coding: utf-8 -*-
class Game:
    def __init__(self, name):
        self.__name = name

    def run(self):
        print('%s running.' % self.__name)
