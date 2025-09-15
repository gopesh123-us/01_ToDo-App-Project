todos = []

print ("Starting a new todo app")

proceed = True

def take_user_input():
    todo = input("Enter to do: \n")
    todos.append(todo.capitalize())

def print_todos(items):
    for i, todo in enumerate(items):
        print(f"{i+1}-{todo.title()}")

take_user_input()

while proceed:
    user_choice = input("\nType add | show | edit | exit: \n")
    match user_choice.strip():
        case "add":
            take_user_input()
            continue
        case "show":
            print("Here is your list of todos: \n")
            print_todos(todos)
            proceed = True
        case "exit":
            print("Bye")
            break;
        case "edit":
            print_todos(todos)
            selected_item = int(input("Which item number do you want to edit? \n"))
            new_item = input("Enter new item name: \n")
            todos[selected_item - 1] = new_item;
            print_todos(todos)
            proceed = True
        case _:
            print("Invalid choice: ")
            continue;

