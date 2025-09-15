todos = [];
proceed = True;

def take_user_input():
    todo = input("Enter to do: \n");
    todos.append(todo.capitalize());

take_user_input();

while proceed:
    user_choice = input("Type add or show or exit: \n");
    match user_choice.strip():
        case "add":
            take_user_input();
            proceed = True;
            continue
        case "show":
            proceed = False;
            print("Here is your list of todos: \n");
            for item in todos:
                item = item.title()
                print(item)
            break;
        case "exit":
            print("Bye");
            break;
        case _:
            print("Invalid choice: ")
            proceed  = True;
            continue;