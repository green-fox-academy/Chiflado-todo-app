import sys
from todo_view import TodoView
from todo_model import TodoModel

class TodoContoller(object):

    def __init__(self):
        self.todo_view = TodoView()
        self.todo_model = TodoModel()
        self.user_command()

    def get_arguments(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return None

    def user_command(self):
        self.arg = self.get_arguments()
        if self.arg == None:
            self.todo_view.print_commands()
        elif self.arg == '-l':
            self.todo_view.print_list(self.todo_model.todo_list)


todo = TodoContoller()