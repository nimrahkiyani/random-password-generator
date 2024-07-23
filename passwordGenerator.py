import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%&()*"

print("This is a random password generator.\nIt takes random length between 7 - 12 .\nYou can also take length on user Input.\n ")

#length = int(input("Enter the length of the password: "))

length = random.randint(7 , 12)
a = "".join(random.sample(password , length ))

print(f"Your password is {a}")

