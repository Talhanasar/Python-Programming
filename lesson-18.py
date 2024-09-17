number_list = [1, 2, 5, 1, 10, 14]

number_list.append(20)
number_list.insert(1, 7)
number_list.remove(2)
number_list.sort()
number_list.reverse()

print(number_list)

print(1 in number_list)
print(12 in number_list)

print(number_list.count(1))

print(number_list.index(10))

number_list2 = number_list.copy()
print(number_list)
print(number_list2)

number_list.pop()
print(number_list)

number_list.clear()
print(number_list)
