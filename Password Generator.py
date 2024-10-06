import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#' ,'$' ,'%', '&', '(', ')', '*', '+']
print('welcome to password generator')
n_letters= int(input("How many letters do you want in your password?\n"))
n_symbols= int(input("How many symbols do you want in your password?\n"))
n_numbers= int(input("How many numbers do you want in your password?\n"))
passwordList=[]
for i in range(1, n_letters+1):
    char=random.choice(letters)
    passwordList += char

for i in range(1, n_symbols+1):
    char=random.choice(symbols)
    passwordList += char

for i in range(1, n_numbers+1):
    char=random.choice(numbers)
    passwordList +=char

print(passwordList)
random.shuffle(passwordList)
print(passwordList)
password = " "
for char in passwordList:
    password += char
print(password)


