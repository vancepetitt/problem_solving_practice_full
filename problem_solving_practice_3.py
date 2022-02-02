#1
# generate random list of numbers
# display the list
# generate target number
# pull number and add other numbers to see if it works
# remove from array if it doesnt
# repeat for all numbers in array
# verify the numbers that give the result / verify that the numbers will not create the target number.

from random import randint, randrange


def array_summation_for_target():
    
    #Array Generation
    print('Generating array of numbers...')
    generated_array = []
    list_length = randrange(1,10)
    for length in range(0, list_length+1, 1):
        generated_array.append(randrange(0,100))
    print(generated_array)
    
    #Target Number
    target_number = int(input('Please enter a target number (positive integer): '))
    if target_number > 0:
        print('Calculating if the array can equal the target number via addition...')
    else:
        target_number = int(input('Please enter a positive integer, silly goose: '))

    # Calculate if the array can produce the target number
    iteration = 1
    target_reached = False
    while target_reached == False:
    #get first number in array
        number_one = generated_array[0]
        position = 1        
    #get next number
        for number in generated_array:
            number_two = generated_array[position]
            sum = number_one + number_two
            if sum == target_number:
                target_reached = True
                print(f'{number_one} and {number_two} will add togeter to reach your target number.')
                break
            elif len(generated_array) == 1:
                target_reached = True
                print('This array cannot generate the target number using addition.')
                break

            elif len(generated_array) > 2:
                next_number_one = iteration - 1
                generated_array.pop([next_number_one])
                iteration += 1
                position = iteration
            else:
                position += 1


array_summation_for_target()



#10
# accept given number
# reverse number
# convert to reciprocal
# calculate and return as decimal

# def reciprocator(number):
#     reversed_number = ''
#     for character in range(len(number)-1, -1, -1):
#         reversed_number += number[character]
#     int_number = int(reversed_number)
#     return print(1/int_number)
    
# reciprocator('25')

