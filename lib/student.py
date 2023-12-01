#!/usr/bin/env python

from user import User

class Student(User):

    def learn(self):
        pass
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = list()
    def learn(self, string_input):
        self.knowledge.append(string_input)