# -*- coding: utf-8 -*-

# Strings are a collection of characters. They are special in that they are immutable
name = "Mitch Labrenz"
print(name[0:5])
print("My name is {}".format(name))

odd_name = ""
sub = 2 if len(name) % 2 == 0 else 3
for i in range(0, int((len(name) - sub) / 2) + 1):
    odd = 2 * i + 1
    odd_name += name[odd]

print(odd_name)

## Assignment, take a string and find out if it is a palendrome.
pal = "Tacocat"
not_pal = "Hello"

def is_palendrome(word):
    word = word.lower()
    i = 0
    rev_word = reversed(word)
    for letter in rev_word:
        if letter != word[i]:
            return False
        i += 1
    return True

def is_pal(word):
    word = word.lower()
    rev_word = word[::-1]
    return rev_word == word

print(is_palendrome(pal) == True)
print(is_palendrome(not_pal) == False)

print(is_pal(pal) == True)
print(is_pal(not_pal) == False)