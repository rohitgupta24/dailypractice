h_letters= []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)


#list_comprehension:
h_letters = [x for x in 'human']
print(h_letters)

#This is the power of list comprehension. It can identify when it receives a string or a tuple and work on it like a list.