n = int(input("Enter a positive number: "))

while n <= 0:
    print("Please enter a positive number.")
    n = int(input("Enter a positive number: "))

total = 0
num = 1

while num <= n:
    total += num
    num += 1

print("Sum =", total)
