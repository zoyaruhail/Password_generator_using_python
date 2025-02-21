import random
def password_generator():
    print("Hello!! Welcome to Password Generator")
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    symbols = "~!@#$%^&*,."
    integers = "1234567890"
    all_char = upper + lower + symbols + integers
    while True:
        try:
            menu = int(input("Select from the options below: \n1. Create Password \n2. Exit\n Your input: "))
            if menu == 1:
                while True:
                    num = int(input("Enter the length of the password you wanted to create (greater than 4): "))
                    if num < 4:
                        print("Passwords should have at four character!!")
                        continue
                    password = [random.choice(upper),random.choice(lower),random.choice(symbols),random.choice(integers)]
                    for _ in range(num-4):
                        password.append(random.choice(all_char))
                    random.shuffle(password)
                    password =  "".join(password)
                    print("Generated Password =", password)
                    break
            elif menu == 2:
                print("Thanks For Using Password Generator!!")
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Only Accepts Integer values")


password_generator()