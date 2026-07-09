import random

#generate a random number
lowest_num = 1
highest_num = 100

random_number = random.randint(lowest_num, highest_num)
print(random_number)

# keep track of the guesses in a list
user_guess_list = []

# Track num of guesses
num_of_guesses = 0

is_playing = True

print("-----Number Guessing Game----")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_playing:
    
    # ask user to guess the number
    user_guess = input("Enter your guess: ")
    print(user_guess)
    if user_guess.isdigit():
        user_guess = int(user_guess)
        num_of_guesses += 1
        if lowest_num > user_guess > highest_num:   
            print(f"{user_guess} is Out of range. Only enter numbers between {lowest_num} and {highest_num}")
        elif user_guess < random_number:
            print("Too Low. Try Again!")
        elif user_guess > random_number:
            print("Too High. Try Again!")
        else:
            print(f"{user_guess} is the correct answer")
            print(f"Num of guesses: {num_of_guesses}")
            is_playing = False
    else:
        print(f"{user_guess} is not a number. Only enter numbers between {lowest_num} and {highest_num}")
    



