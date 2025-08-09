my_list = []
numbers = [10, 20, 30, 40]

for num in numbers:
    my_list.append(num)

my_list.insert(2, 15)
print(my_list)

numbers = [50, 60, 70]
my_list.extend(numbers)
print(my_list)

my_list.remove(70)
print(my_list)

my_list.sort()
print(my_list)

print(my_list[3])


