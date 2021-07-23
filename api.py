import app
import requests
import pdb


class API:
    def __init__(self, data):
        self.data = data

    def exercise(self):
        return str(self.data['a']) + self.data['op'] + str(self.data['b'])

    def calculate(self):
        if self.data['op'] == "+":
            res = self.data['a'] + self.data['b']
        elif self.data['op'] == "-":
            res = self.data['a'] - self.data['b']
        elif self.data['op'] == "*":
            res = self.data['a'] * self.data['b']
        return res
