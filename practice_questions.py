# Question 1
list = [1, 2, 3, 4, 5]
print(list)
list.append(6)
print(list)

# Question 2
tuple = (1, 2, 3, 4, 5)
set = {1, 2, 3, 4, 5}

print(tuple[:3])

for i in set:
    if i > 3:
        break
    print(i)
# Or turn it into a list

# Question 3
shopping_dict = {'apple': 1.99, 'books': 4.99, 'broccoli': 1.99}
print(type(shopping_dict))
print(shopping_dict)

# increasing price of books
shopping_dict['books'] = 6.99
print(shopping_dict)

# for i, j in shopping_dict.items():
#     print(j)

# Question 4
# increasing price of books
shopping_dict['books'] = 6.99
print(shopping_dict)

# Question 5
def add(arg1, arg2):
    return arg1 + arg2

print(add(2, 4))

# Question 6
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

test = Person('Matthew', '21')
print(test.name)
print(test.age)

class Student(Person):
    def __init__(self,name, age, student_id, course):
        # The super() method allows one to access attributes and methods from the parent class
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

student = Student('Matthew', 22, 1, 'DevOps')
print(student.name, student.age, student.student_id, student.course)

# Question 7
shopping_dict_2 = {'fruits': 5.99, 'veggies': 2.99, 'meat': 6.99}
print(shopping_dict_2)

# Get total cost of values in dict
print(sum(shopping_dict_2.values()))

# Question 8
def add_dict(arg):
    return sum(arg.values())

print(add_dict(shopping_dict_2))

# Question 9
# The super() method allows one to access attributes and methods from the parent class
shopping_dict_2 = {'fruits': 5.99, 'veggies': 2.99, 'meat': 6.99}

# Add another item to dict before veggies
# YOU CANT DICTS YOU CANNOT ADD BY INDEX
# Can only add bread to the end of dict
shopping_dict_2['bread'] = 0.99
print(shopping_dict_2)

# Question 10
shopping_list = ['fruits', 'veggies', 'meat', 'bread']
print(shopping_list)

# Print items up to bread
for item in shopping_list:
    if item == 'bread':
        break
    print(item)

