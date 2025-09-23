# Calculate the area of a rectangle with length 7 and width 3.

def area_of_rectangele(length, width):
    return length * width

print(area_of_rectangele(7, 3))

# Reverse the string "Python" using slicing.
def reverse_string(string):
    return string[::-1]
print(reverse_string("Python"))

# Write a function get_domain(email) that:
# Takes a string like "alice@gmail.com"
# Returns only "gmail.com"
def get_domain(email):
    return email.split("@")[-1]
print(get_domain("alice@gmail.com"))

# Extract first + last name
# Given "Ada Lovelace", write code to print:
def extract_names(full_name):
    first_name, last_name = full_name.split(" ")
    return f"First: {first_name}, Last: {last_name}"
print(extract_names("Ada Lovelace"))

# Truncate a sentence
# Take the string:sentence = "Python is fun to learn and practice"
# Use split() to get only the first 3 words.
# Join them back into "Python is fun".
def truncate_sentence(sentence, num_words):
    words = sentence.split(" ")
    truncated = " ".join(words[:num_words])
    return truncated
print(truncate_sentence("Python is fun to learn and practice", 3))

# Create a list of numbers 1–5 and remove the number 3.
def remove_number(numbers, number_to_remove):
    numbers.remove(number_to_remove)
    return numbers
print(remove_number([1, 2, 3, 4, 5], 3))


# Create a dictionary for a book: title, author, pages.
def create_book_dict(title, author, pages):
    book = {
        "title": title,
        "author": author,
        "pages": pages 
    }
    return book
print(create_book_dict("1984", "George Orwell", 328))

# Print all even numbers from 1 to 20.
def print_even_numbers(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
# print_even_numbers(20)

def even_numbers(num):
    i = 1
    while i <= num:
        if i % 2 == 0:
            print(i)
        i += 1
# even_numbers(20)

def squares(num):
    # Using list comprehension
    # squares = [x**2 for x in range(num + 1)]
    # return squares
    squares = []
    for x in range(num + 1):
        squares.append(x**2)
    return squares
print(squares(5))

# Calculate the factorial of a number (e.g., 5! = 5 * 4 * 3 * 2 * 1).
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))

# prefer this one
def factorial2(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result
print(factorial2(5))

# Create a Car class with attributes make, model, and a method drive() that prints "Driving {make} {model}".
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving {self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.drive()
