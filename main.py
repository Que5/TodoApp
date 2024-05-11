import functions

while True:
    user_action = input("Type add, show, edit or exit, done: ")
    user_action = user_action.strip()
    user_action = user_action.lower()
 
    
    if user_action.startswith('add'):
            todo = user_action[4:]

            todos = functions.get_todo()

            todos.append(todo + '\n')
            functions.write_todos(todos)

    elif 'show' in user_action:
            todos = functions.get_todo()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item.capitalize()}."
                print(row)
    elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                print(number)
                number = number - 1

                todos = functions.get_todo()


                new_to_do = input("Enter new todo: ")
                todos[number] = new_to_do + "\n"

                functions.write_todos(todos)
            except ValueError:
                print('Your command in not valid!')
                continue

    elif user_action.startswith('done'):
            try:
                number = int(user_action[5:])
                

                todos = functions.get_todo()
                index = number - 1
            
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                todos.pop(number)
                functions.write_todos(todos)

                message = F'Todo {todo_to_remove} was removed from the list!'
                print(message)
            except IndexError:
                 print("There is no item with that number.")
                 continue

    elif user_action.startswith('exit'):
            break
    else:
         print("Invalid selection")
        
        

print("Thank you")
    
  