# 1 Happy Numbers

#Steps:
# start wth a number
# get digit's sum of squares
# check to see if those digits are one, or if they are the original number.
# If not, reset and run the new number.
# continue until digits are either: 1, the original number, or a sum seen before.

def happy_number_check():
    original_number = input('Please enter a positive integer: ')
    list_of_sum_squares = [original_number,]
    calculation_number = original_number
    sum_squares = 0
    determined = False
    while determined is False:
        for digit in calculation_number:
            integer = int(digit)
            square = integer * integer
            sum_squares += square
        
        if sum_squares == 1:
            determined = True
            print('This is a happy number! :)')
        elif sum_squares in list_of_sum_squares:
            determined = True
            print('This is a sad number! :(')
        else:
            list_of_sum_squares.append(sum_squares)
            calculation_number = str(sum_squares)
            sum_squares = 0

happy_number_check()

#2 Prime numbers

#Steps:
# get number between 0 and 100
# test to see if it is divisible by any numbers between 1 and itself
# if at any point modulus is equal to 0, the number is no longer prime.
# if the range check completes, the number is prime.

def prime_number_check():
    prime = True
    input_number = int(input('Please enter an integer between 0 and 100: '))
    if input_number <= 0 or input_number > 100:
        input_number = int(input('Sorry, please enter an integer between 0 and 100: '))
    print('Calculating......')
    for number in range(2, input_number, 1):
        remainder = input_number % number
        if remainder == 0:
            prime = False
            print(f'{input_number} is NOT a prime number!')
            break
    if prime == True:
        print(f'{input_number} is a prime number!')
        
prime_number_check()

#3 Fibonnaci

#Steps
# input starting number
# input how many iterations so it doesnt go on forever
# first number doesnt exist yet, start at 0.
# create variable for the two proceeding numbers.
# create a term for the sum of those numbers.
# calcuate sum
# move 1st preceeding to 2nd preceeding
# move sum to 2nd preceeding.
# new iteration
# repeat for every iteration.

def fibonacci_sequencer():
    input_number = int(input('Please enter a starting number: '))
    stop_iteration = int(input('How many Fibonacci iterations do you want to calculate?: '))
    iteration = 0
    first_number = 0
    second_number = input_number
    print(second_number)
    for iteration in range(0, stop_iteration, 1):
        sum = first_number + second_number
        print(sum)
        first_number = second_number
        second_number = sum
        iteration += 1

fibonacci_sequencer()
