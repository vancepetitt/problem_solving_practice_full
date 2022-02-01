#1 Reverse a string
def reverse_word(word):
    reversed_word = ''
    for letter in range(len(word)-1, -1, -1):
        reversed_word += word[letter]
    return print(reversed_word)

reverse_word('fish')

#2 Capitalize Letter
def first_letter_capitalizer():
    string = 'please capitalize this statement for me'
    capitalized_string = ''
    previous_character = ' '
    for character in string:
        if previous_character == ' ':
            new_character = character.upper()
            capitalized_string += new_character
            previous_character = character
        else:
            capitalized_string += character
            previous_character = character

    print(capitalized_string)

first_letter_capitalizer()

#3
def compressor():
    string = input('Please enter a string for compression: ') + ' '
    previous_character = ' '
    count = 0
    compressed_string = ''
    for character in string:
        if previous_character == character or previous_character == ' ':
            count += 1
            previous_character = character
        else:
            compressed_string += str(count)
            compressed_string += previous_character
            count = 1
            previous_character = character
    print(compressed_string)

compressor()

# Bonus Challenge: Palindrome
def palindrome_check(word):
    reversed_word = ''
    for letter in range(len(word)-1, -1, -1):
        reversed_word += word[letter]
    
    if reversed_word == word:
            print('Palindrome')
    if reversed_word != word:
            print('Not a palindrome')

palindrome_check('racecar')
