random_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 15, 25, 35, 45, 55, 65, 75, 85, 95, 2, 4, 6, 8, 12, 14, 16, 18 ,22, 24, 26, 28, 32, 34, 36, 38, 42, 44, 46, 48, 52, 54, 56, 58, 62, 64, 66, 68, 72, 74, 76 ]
print(random_numbers)

numbers_greater_than_50 = list(filter(lambda x: x > 50, random_numbers))
print("Numbers greater than 50:", numbers_greater_than_50)

divisible_by_7 = list(filter(lambda x: x % 7 == 0, random_numbers))
print("Numbers divisible by 7 are:")
print(divisible_by_7)

double_digit_numbers = list(filter(lambda x: 10 <= x < 100, random_numbers))
print("Double_digit_numbers are:")
print(double_digit_numbers)

matching_numbers = list(filter(lambda x: 10 <= x < 100 and (x // 10) == (x % 10), random_numbers))
print("Two-digit numbers where the ones digit equals the tens digit are:")
print(matching_numbers)

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
numbers_with_sum_9 = list(filter(lambda x: sum_of_digits(x) == 9, random_numbers))
print("numbers where the sum of their digits is 9 are:")
print(numbers_with_sum_9)

# Calculate the average of the numbers
average = sum(random_numbers) / len(random_numbers)
numbers_larger_than_average = list(filter(lambda x: x > average, random_numbers))
print(f"The average of the numbers is: {average:.2f}")
print("Numbers larger than the average are:")
print(numbers_larger_than_average)

max_number = max(random_numbers)
half_max = max_number / 2
numbers_greater_than_half_max = list(filter(lambda x: x > half_max, random_numbers))
print(f"The maximum number is: {max_number}")
print(f"Half of the maximum number is: {half_max:.2f}")
print("Numbers greater than half of the maximum number are:")
print(numbers_greater_than_half_max)


# Exr 2

games = [,"V Auto Theft Grand ","Fortnite","The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

#name longer than eight letters
long_name_game = list(filter(lambda n: len(n) > 8),games)
print(long_name_game)

#game name starts with F
f_names = list(filter(lambda n: n.startswith('F'),games))
print(f_names)

# two words game name
two_words_name = list(filter(lambda n : len(n.split()) == 2, games ))
print(two_words_name)

 1
