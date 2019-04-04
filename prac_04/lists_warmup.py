numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])  # 3
print(numbers[-1])  # unknown
print(numbers[3])  # 1
print(numbers[:-1])  # unknown
print(numbers[3:4])  # unknown
print(5 in numbers)  # True
print(7 in numbers)  # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = 10
print(numbers)

numbers[6] = 1
print(numbers)

elements = numbers[2:]
print(elements)

print(9 in numbers)