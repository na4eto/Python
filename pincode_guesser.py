import random
import string

digits = list(string.digits)
iteration_counter = 0

phone_pass = input('Enter PIN: ')

guesser = ''

while guesser != phone_pass:
    guesser = random.choices(digits, k=len(phone_pass))
    iteration_counter += 1
    print(f">>>{''.join(guesser)}<<<")

    if guesser == list(phone_pass):
        print(f"Your password is {''. join(guesser)}"
            f"\nNumber of guess counter iteration is: {iteration_counter}")
        break
