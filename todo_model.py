
class TodoModel(object):

    def __init__(self):
        self.todo_list = []
        with open('todo_list.txt', 'r') as self.file:
            for i in self.file:
                self.todo_list.append({'checked': i[0] == '1', 'name': i[1:].rstrip('\n')}) 