# lists

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# add item
fruits.append("pineapple")
print(fruits)
# remmove item
# fruits.remove(fruits[2])
# print(fruits)
# fruits.remove("pineapple")
# print(fruits)
# fruits.pop(2)
# print(fruits)
# fruits[1] = "grape"
# print(fruits)
print(len(fruits))
print(fruits[-1])
print(fruits[0:2])

# tuple
coordinates = (10, 20)
print(coordinates[0])
# coordinates[0] = 15 # This will raise an error because tuples are immutable
print(len(coordinates))

numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
for num in numbers:
    print(num)

# dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(student["name"])
print(student.get("age"))

student["age"] = 21
print(student)
student["gpa"] = 3.8
print(student)
print(student["gpa"])

for key, value in student.items():
    print(key, value)

data = {}
data["a"] = 1
data["a"] += 2

print(data)
for key, value in data.items():
    print(key, value)
          
for number in range(5):
    print(number)

count = 0

while count < 3:
    print(count)
    count += 1

for num in range(5):
    if num == 3:
        break

    print(num)

def hello(name):
    return f"Hello, {name}!"
print(hello("Cy"))