print("\033c")

def square(a, b):
    squareList = []
    
    for i in range(a, b + 1):
        squareList.append(i ** 2)
    
    return squareList

def odd(x):
    oddList = []
    
    for j in x:
        if j % 2 == 1:
            oddList.append(j)
    
    return oddList

def even(y):
    evenList = []
    
    for k in y:
        if k % 2 == 0:
            evenList.append(k)
    
    return evenList

start = int(input("Enter the first number : "))
end = int(input("Enter the last number : "))

squareNumbers = square(start, end)

oddNumbers = odd(squareNumbers)
evenNumbers = even(squareNumbers)

print(f"\nThe square of numbers from {start} to {end} are {squareNumbers}")

print(f"\nThe odd numbers from {squareNumbers} are {oddNumbers}.")
print(f"The even numbers from {squareNumbers} are {evenNumbers}.")