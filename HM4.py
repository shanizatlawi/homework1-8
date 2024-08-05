fruits = ["Appel", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

print("The original list of fruits is:")
print(fruits)

reversed_fruits = list(map(lambda fruit: fruit[::-1], fruits))

print("The list of fruits with each name reversed is:")
print(reversed_fruits)

first_letters = list(map(lambda fruit: fruit[0], fruits))

print("The list of the first letters of each fruit is:")
print(first_letters)

capital_letters_fruits = list(map(lambda fruit: fruit.upper(),fruits))
print("The list of fruits in capital letters is:")
print(capital_letters_fruits)

fruit_lengths = list(map(lambda fruit: len(fruit), fruits))

print("The list of the lengths of each fruit name is:")
print(fruit_lengths)



