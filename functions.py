FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_file:
        todos_local = file_file.readlines() 
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_file:
        file_file.writelines(todos_arg) 
  
