print("---- Use your Calculator now ----")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation you want to perform :\n")

print("1. Addition")
print("2. Subtractraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = input("Enter your choice (1/2/3/4/5): \n")

if choice == '1':
    print(f"The Addition of {num1} and {num2} is :" ,num1 + num2)
elif choice == '2':
    print(f"The Subtractraction of {num1} and {num2} is :", num1 - num2)
elif choice == '3':
    print(f"The Multiplication of {num1} and {num2} is :", num1 * num2)
elif choice == '4':
    print(f"The Division of {num1} and {num2} is :", num1 / num2)
elif choice == '5':
    print(f"The Modulus of {num1} and {num2} is :", num1 % num2)
else:
    print("You choose an invalid operation ! :")