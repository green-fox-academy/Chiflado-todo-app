import sys


class TodoApp(object):

    def __init__(self):
        self.commands = [
            {'arg': '-l', 'desc': 'Lists all the tasks'},
            {'arg': '-a', 'desc': 'Adds a new task'},
            {'arg': '-r', 'desc': 'Removes a task'},
            {'arg': '-c', 'desc': 'Completes a task'}
        ]
    def print_commands(self):
        print('Command Line Todo application\n' + 
              '==============================\n\n' + 
              'Command line arguments:')
        for i in self.commands:
            print(i['arg'] + '  ' + i['desc'])


def start_app():
    app = TodoApp()
    args = sys.argv[1:]
    if not args:
        app.print_commands()

start_app()