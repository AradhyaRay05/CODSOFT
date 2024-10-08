import string
import random

print("----- Welcome to PASSWORD GENERATOR -----\n")

words = [random.choice(string.ascii_letters) for i in range(int(input('Enter how many letters you want to input: ')))]
numbers = [random.choice(string.digits) for i in range(int(input('Enter how many numbers you want to input: ')))]
symbol = [random.choice(string.punctuation) for i in range(int(input('Enter how many symbols you want to input: ')))]
key = words + numbers + symbol
random.shuffle(key)

input_length = int(input("Enter the desired length of the password: "))

if input_length > len(key):
    print(f"The desired length exceeds the available characters.Random password is possible using this maximum length: {len(key)}")
    input_length = len(key)

password = ''.join(key[:input_length])
print(f"Generated Password: {password}")