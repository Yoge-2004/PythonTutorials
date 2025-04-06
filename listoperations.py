from functools import reduce
import copy

print("===== Number List Operations =====")

# Initializing a list
numbers_list = list(map(int, input("Enter the list elements separated by comma and space: ").split(', '))) \
    if bool(int(input("Do you want to give elements?\nEnter 1 for Yes or 0 for No: "))) else [x for x in range(1, 101)]

print("List:", numbers_list)

# Basic properties
print("Sum:", sum(numbers_list))
print("Maximum:", max(numbers_list))
print("Minimum:", min(numbers_list))
print("Count of even numbers:", len([x for x in numbers_list if x % 2 == 0]))

# Target count
target = int(input("Enter the target: "))
print(f"Occurrences of {target}: {numbers_list.count(target)}")

# Reverse and Palindrome
reversed_list = numbers_list[::-1]
print("Reversed List:", reversed_list)
print("Is Palindrome?", "Yes" if numbers_list == reversed_list else "No")

# Remove duplicates
unique_list = list(set(numbers_list))
print("Removed Duplicates:", unique_list)

# Sort operations
numbers_list.sort()
print("Sorted List:", numbers_list)
numbers_list.sort(reverse=True)
print("Reverse Sorted List:", numbers_list)
numbers_list.sort()

print("Second Largest Number:", numbers_list[-2])
print("Second Smallest Number:", numbers_list[1])

# Positives and Negatives
positive_numbers = [x for x in numbers_list if x >= 0]
negative_numbers = [x for x in numbers_list if x < 0]
print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)

# Multiply all elements
result = reduce(lambda x, y: x * y, numbers_list, 1)
print("Multiplication Result:", result)

# Filter divisible by 3
filtered_list = list(filter(lambda x: x % 3 == 0, numbers_list))
print("Divisible by 3:", filtered_list)

# Merging and comparisons
merged_list = numbers_list + unique_list
print("Merged List:", merged_list)

common_elements = [x for x in numbers_list if x in unique_list]
print("Common Elements:", common_elements)

unique_elements = [x for x in numbers_list if x not in unique_list]
print("Unique Elements from numbers_list:", unique_elements)

print("Difference between Max and Min:", max(numbers_list) - min(numbers_list))
print("All elements are unique?", len(set(numbers_list)) == len(numbers_list))

# Replace even and odd numbers
replaced_even_numbers = [1 if x % 2 == 0 else x for x in unique_list]
print("Even Numbers Replaced with 1:", replaced_even_numbers)

replaced_odd_numbers = [1 if x % 2 != 0 else x for x in unique_list]
print("Odd Numbers Replaced with 1:", replaced_odd_numbers)

# Index operations
element = int(input("Enter the element to be searched: "))
if element in unique_list:
    print(f"Index of {element} in list:", unique_list.index(element))
else:
    print(f"{element} not found in list.")

print(f"All indexes of {element}:", [i for i, x in enumerate(unique_list) if x == element])

# Elements greater and lesser than a value
value = int(input("Enter a value: "))
print(f"Elements greater than {value}:", list(filter(lambda x: x > value, unique_list)))

value = int(input("Enter another value: "))
print(f"Elements lesser than {value}:", list(filter(lambda x: x < value, unique_list)))

# Remove evens and odds
print("Removed Even Numbers:", list(filter(lambda x: x % 2 != 0, unique_list)))
print("Removed Odd Numbers:", list(filter(lambda x: x % 2 == 0, unique_list)))

# Membership check
element = int(input("Enter a value to check presence: "))
print(f"Is {element} in list?", element in unique_list)

# Average
print("Average of List:", sum(unique_list) / len(unique_list))

# ==================== String List Operations ====================
print("\n===== String List Operations =====")

strings = [chr(x) for x in range(97, 123)]

upper_strings = [s.upper() for s in strings]
print("Uppercase Strings:", upper_strings)

lower_strings = [s.lower() for s in strings]
print("Lowercase Strings:", lower_strings)

strings = ["Hi", "Hello", "Python", "", "I am GPT"]

# Count strings longer than 3
count = len(list(filter(lambda x: len(x) > 3, strings)))
print("Strings with length > 3:", count)

# Concatenate all strings
concatenated_string = reduce(lambda x, y: x + y, strings, "")
print("Concatenated String:", concatenated_string)

# Longest and shortest strings
print("Longest String:", max(strings, key=len))
print("Shortest String:", min(strings, key=len))

# Remove empty strings
print("Non-Empty Strings:", list(filter(lambda x: x != "", strings)))

# Strings starting and ending with vowels
count_start_vowel = len(list(filter(lambda x: str.lower(x[0]) in 'aeiou', strings if x else "")))
print("Strings starting with vowels:", count_start_vowel)

count_end_vowel = len(list(filter(lambda x: str.lower(x[-1]) in 'aeiou', strings if x else "")))
print("Strings ending with vowels:", count_end_vowel)

# Add element at end
element = input("Enter an element to be added: ")
numbers_list.append(element)
print("Updated List:", numbers_list)

# Insert element at position
position = int(input("Enter position to insert element: "))
numbers_list.insert(position, element)
print("After Insertion:", numbers_list)

# Delete by value
numbers_list.remove(element)
print(f"After removing {element}:", numbers_list)

# Delete by index
index = int(input("Enter index to remove element: "))
if index < len(numbers_list):
    print(f"Removed {numbers_list.pop(index)} at index {index}: ", numbers_list)

# Copy and clear
copied_list = copy.deepcopy(unique_list)
print("Copied List:", copied_list)

copied_list.clear()
print("Cleared List:", copied_list)

# Count total characters
print("Total characters in string list:", len(concatenated_string))

# Strings with more than one word
sentences = list(filter(lambda x: len(x.split(' ')) > 1, strings))
print("Multi-word Strings:", sentences)

# Capitalize strings
capitalized_strings = list(map(str.capitalize, strings))
print("Capitalized Strings:", capitalized_strings)
