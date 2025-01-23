print("\033c")

l = [4, 5, 1, 2, 9, 7, 10, 8]
print(f"Original list : {l}")

sum = 0
for i in l:
    sum += i

print(f"sum = {sum}")

avg = sum / len(l)
print(f"average = {avg}")

print()

l.sort()
print(f"Sorted list : {l}")

print(f"Smallest element is : {l[0]}")
print(f"Largest element is : {l[-1]}")