string = "python"
for character in string:
    print(character)

grocery_list = ["egg", "rice", "oil"]
for item in grocery_list:
    print(item)

for number in range(10):
    print(number)

for number in range(5, 10):
    print(number)

for number in range(5, 10, 2):
    print(number)

bills = [10, 30, 50, 10]
total = 0
for bill in bills:
    total += bill

print(f"Total bill: ${total}")
