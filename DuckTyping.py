"""
Duck Typing is a term commonly related to dynamically typed programming languages and polymorphism.
The idea behind this principle is that the code itself does not care about whether an object is a duck,
but instead it does only care about whether it quacks
"""


class Pycharm:
    def execute(self):
        print("I am Pycharm")


class Vscode:
    def execute(self):
        print("I am VS Code")


class Myide:
    def compile(self, ide):
        ide.execute()


myide = Myide()

ide = Pycharm()
myide.compile(ide)

ide = Vscode()
myide.compile(ide)
