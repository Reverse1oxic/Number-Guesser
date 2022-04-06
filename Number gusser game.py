def number_guesser():
    number = 62
    guess_count = 3
    number_of_guess = 0
    try:
        guess = input("Guess: ")
        while guess != number:
            number_of_guess += 1
            if number_of_guess != guess_count:
                guess = float(input("Guess: "))
            if number_of_guess == guess_count:
                print("You lost try again")
                break   
            if guess == number:
                print("You won!!")
                break        
    except ValueError:
        print("You have entered an invalid charecter try again!")
    
number_guesser()