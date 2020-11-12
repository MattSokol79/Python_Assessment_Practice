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

for i, j in shopping_dict.items():
    print(j)

# Question 4
