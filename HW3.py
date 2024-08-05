import random

# Generate a list of 20 random numbers between -50 and 50

random_numbers = [random.randint(-50, 50) for _ in range(20)]

print("The list of 20 random numbers between -50 and is:")
print(random_numbers)


power_numbers = list(map(lambda x: x ** 3, random_numbers))

print("The list of numbers rased to the power of 3 is:")
print(power_numbers)


unity_digits = list(map(lambda x: abs(x) % 10, random_numbers))

print("the unity digit of each number is:")
print(unity_digits)


fahrenheit_numbers = list(map(lambda x: (x * 9/5) + 32, random_numbers))

print("the list of numbers converted to Fahrenheit is:")
print(fahrenheit_numbers)


transformed_numbers = list(map(lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero", random_numbers))

print("The list with positive numbers replaced by 'positive' and negative numbers replaced by 'negative' is:")
print(transformed_numbers)


max_number = max(random_numbers)
min_number = min(random_numbers)

transformed_numbers = list(map(lambda x: "max" if x == max_number else "min" if x == min_number else x, random_numbers))

print("The list with the largest number replaced by 'max' and the smallest number replaced by 'min' is:")
print(transformed_numbers)
