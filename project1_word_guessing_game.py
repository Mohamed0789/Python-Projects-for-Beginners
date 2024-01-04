# Simple word guessing game project
"""
.Build a Number guessing game, in which the user selects a range.
.Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
.Some random integer will be selected by the system and the user has to guess that
integer in the minimum number of guesses

- the minimum number of guesses depends upon range. And the compiler must calculate the
minimum number of guessing depends upon the range, on its own. For this, we have a formula:-
( Minimum number of guessing = log2(Upper bound – lower bound + 1))

- Steps:
    .User inputs the lower bound and upper bound of the range.
    .The compiler generates a random integer between the range and store it in a variable for future references.
    .For repetitive guessing, a while loop will be initialized.
    .If the user guessed a number which is greater than a randomly selected number, the user gets an output
     “Try Again! You guessed too high“
    .Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output
     “Try Again! You guessed too small”
    .And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
    .Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get
     “Better Luck Next Time!” output.
"""
import math
import random


def guess_num(lower, upper, min_guess_num):
    random_number = random.randint(lower, upper)
    cnt = 0
    while True:
        num_from_user = int(input("Guess a number : "))
        if num_from_user < random_number:
            print("Try Again! You guessed too small")
        elif num_from_user > random_number:
            print("Try Again! You guessed too High")
        elif num_from_user == random_number:
            cnt += 1
            print(f"Congratulations You did it in {cnt} try")
            break
        cnt += 1
        if cnt > min_guess_num:
            print(f"Better Luck Next Time! your count{cnt} exceeded the min guess number")


if __name__ == '__main__':
    lower_bound = int(input("Enter Lower bound: "))
    upper_bound = int(input("Enter Upper bound: "))

    min_guess_num = round(math.log(upper_bound - lower_bound + 1, 2))
    print(f"\t you have only {min_guess_num} chances to Guess the number ! ")
    guess_num(lower_bound, upper_bound, min_guess_num)
