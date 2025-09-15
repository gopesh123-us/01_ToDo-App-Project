proceed = True;
names = [];
while proceed:
    user_name = input("Enter your name: \n");
    print(user_name);
    names.append(user_name.capitalize())
    user_quit = input("Do you want to quit ? (y/n)");
    if user_quit == "y":
        proceed = False;
        print("Thank you for your entering your name");
        print("Here are all the names you entered:");
        print(names);


