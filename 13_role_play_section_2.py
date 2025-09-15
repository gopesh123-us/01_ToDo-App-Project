pwd = "Gopesh"
user_input = input("Please enter password: ");

match user_input:
    case "Gopesh":
        print("Correct")
    case _:
        print("Incorrect")


fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)