
class TodoModel(object):

    def __init__(self):
        self.todo_list = []
        with open('todo_list.txt', 'r') as self.list_file:
            for i in self.list_file:
                self.todo_list.append({"checked": line[0] == "1", "name": line[2:].rstrip("\n")}) 