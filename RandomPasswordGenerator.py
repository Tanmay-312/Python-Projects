import random
import string

print("Hello, Lets create a Strong Password for you")

length_of_password = int(input("Enter the length of the password you want to generate: "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

the_data = lower_letters + upper_letters + number + symbols

choose = random.sample(the_data, length_of_password)
password = "".join(choose)
print(password)
