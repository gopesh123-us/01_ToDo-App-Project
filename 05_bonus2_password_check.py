password = "Happy";
proceed = True;
while proceed:
    user_pass = input("Enter your password: ");
    if user_pass == password:
        print("correct password");
        proceed = False;

