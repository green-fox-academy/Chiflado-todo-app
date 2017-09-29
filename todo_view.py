
class TodoView(object):

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

    def print_list(self, todo_list):
        if len(todo_list) == 0:
            print('No todos for today! :)')
        else:
            for i in range(len(todo_list)):
                task = todo_list[i]['name']
                check = 'x' if todo_list[i]['checked'] else ' '
                print(str(i+1) + ' - [' + check + '] ' + task)
