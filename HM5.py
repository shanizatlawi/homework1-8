
cities = [
    "Tokyo",
    "New York",
    "Paris",
    "London",
    "Sydney",
    "Dubai",
    "Shanghai"
]

print("The original list of cities is:")
print(cities)


sorted_by_length = sorted(cities, key=lambda city: len(city))
print("\nThe list of cities sorted by the length of the city name is:")
print(sorted_by_length)


sorted_by_last_letter = sorted(cities, key=lambda city: city[-1])
print("\nThe list of cities sorted by the last letter of the city name is:")
print(sorted_by_last_letter)


sorted_by_reverse_alphabetical = sorted(cities, key=lambda city: city[::-1])
print("\nThe list of cities sorted by the name of the city in reverse alphabetical order is:")
print(sorted_by_reverse_alphabetical)



