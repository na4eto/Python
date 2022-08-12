import random
from string import digits, ascii_lowercase, ascii_uppercase

all_combinations_from_digits_letters_ponctuation = ascii_lowercase + ascii_uppercase + digits

num_of_passwords = int(input('Enter the amount of passwords that you would like to create: '))

while num_of_passwords > 10:
    print("Error! Passwords can't be more than 10")
    num_of_passwords = int(input('Try again: '))
while num_of_passwords < 1:
    print("The number of passwords can't be a negative number. Or zero")
    num_of_passwords = int(input('Try again: '))

if num_of_passwords == 0 or num_of_passwords < 0:
    print('Error')
    quit()
password_length = int(input('Enter the pass length: '))
while password_length <= 0:
    password_length = int(input('Enter a valid password length: '))

pass_num = 1

for x in range(0, num_of_passwords):
    password = ''.join(random.sample(all_combinations_from_digits_letters_ponctuation, password_length))
    if num_of_passwords == 1:
        print(f'Your password is: {password}')
    elif 1 < num_of_passwords <= 10:
        print(f'Password {pass_num} is: {password}')
    else:
        print("Error! Passwords can't be more than 10")
        quit()
    pass_num += 1
