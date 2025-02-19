# FOR LOOP
print("For Loop - Counting Down")
for i in range(5, 0, -1):  # Reverse counting from 5 to 1
    print(i)

# WHILE LOOP
print("\nWhile Loop - Multiples of 2")
x = 2
while x <= 10:
    print(x)
    x += 2  # Incrementing by 2

# BREAK STATEMENT
print("\nBreak Statement - Stop at 5")
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)

# CONTINUE STATEMENT
print("\nContinue Statement - Skip 4")
for i in range(7):
    if i == 4:
        print("Skipping", i)
        continue
    print(i)

# NESTED LOOP
print("\nNested Loop - Printing a Pattern")
for i in range(1, 4):  
    for j in range(1, i + 1):  
        print("*", end=" ")  
    print()  # New line after each row

# LOOP WITH ELSE STATEMENT
print("\nLoop With Else Statement - Checking prime")
num = 7
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
else:
    print(f"{num} is a prime number!")  
