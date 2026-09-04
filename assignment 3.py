# Create a simple program that uses a while loop to iterate over a range of numbers from 1 to 10.

num = 1

# Loop through numbers from 1 to 10
while num <= 10:

    
    if num == 8:
        break

    if num % 2 != 0:
        num += 1
        continue
    print(num)

    num += 1