min = 0
max = 100
guess =(max + min) / 2
user_input = ""
print "Please think of a number between 0 and 100!"
while user_input != 'c':
    print "Is your secret number " + str(guess) + "?"
    user_input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == "l":
        min = guess
        guess = (max + min) / 2
    elif user_input == "h":
        max = guess
        guess = (max + min) / 2
    elif user_input == "c":
        break
    else:
        print "Sorry, I did not understand your input."

print "Game over. Your secret number was: " + str(guess)
