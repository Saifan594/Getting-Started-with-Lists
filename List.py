print("\033c")

emptyList = []
print(emptyList)
print(type(emptyList))

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[2])

numbers.pop()
numbers.pop()
print(numbers)

numbers.append("Saifan")
numbers.append("Nahian")
print(numbers)

triples = [1, 2, 3] * 3
print(triples)

aList = [100, 200, 300, 400, 500]
print(aList[::-1])