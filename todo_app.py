import sys


class TodoApp(object):

    def __init__(self):
        self.commands = [
            {'arg': '-l', 'desc': 'Lists all the tasks'},
            {'arg': '-a', 'desc': 'Adds a new task'},
            {'arg': '-r', 'desc': 'Removes a task'},
            {'arg': '-c', 'desc': 'Completes a task'}
        ]
