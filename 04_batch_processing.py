message = "Enter todo:\n";
x = 0;
todos = [];
while x < 3:
    todo = input(message);
    todo = todo.capitalize();
    todos.append(todo);
    print(todos);
    x = x + 1;

sentence = "the sky is blue today."
print(sentence.capitalize())
name = "sarah smith"
print(name.title())


