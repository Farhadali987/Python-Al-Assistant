# ARITHMETIC OPERATORS  
print("Arithmetic Operators")  
x, y = 15, 4  

# Addition  
print(f"Addition: {x} + {y} = {x + y}")  

# Subtraction  
print(f"Subtraction: {x} - {y} = {x - y}")  

# Multiplication  
print(f"Multiplication: {x} * {y} = {x * y}")  

# Division (returns float)  
print(f"Division: {x} / {y} = {x / y}")  

# Exponentiation (Power)  
print(f"Exponentiation: {x} ** {y} = {x ** y}")  

# Modulus (Remainder)  
print(f"Modulus: {x} % {y} = {x % y}")  

# Floor Division (Removes decimal)  
print(f"Floor Division: {x} // {y} = {x // y}")  


# ASSIGNMENT OPERATORS  
print("\nAssignment Operators")  
z = 20  

# Addition assignment  
z += 5  
print(f"z += 5 -> {z}")  

# Subtraction assignment  
z -= 3  
print(f"z -= 3 -> {z}")  

# Multiplication assignment  
z *= 2  
print(f"z *= 2 -> {z}")  

# Division assignment  
z /= 4  
print(f"z /= 4 -> {z}")  

# Exponentiation assignment  
z **= 2  
print(f"z **= 2 -> {z}")  

# Modulus assignment  
z %= 5  
print(f"z %= 5 -> {z}")  

# Floor division assignment  
z //= 2  
print(f"z //= 2 -> {z}")  


# COMPARISON OPERATORS  
print("\nComparison Operators")  
a, b = 7, 10  

print(f"{a} == {b} -> {a == b}")  # Equal  
print(f"{a} != {b} -> {a != b}")  # Not Equal  
print(f"{a} > {b} -> {a > b}")    # Greater  
print(f"{a} < {b} -> {a < b}")    # Less  
print(f"{a} >= {b} -> {a >= b}")  # Greater or Equal  
print(f"{a} <= {b} -> {a <= b}")  # Less or Equal  


# LOGICAL OPERATORS  
print("\nLogical Operators")  
c, d = True, False  

print(f"{c} and {d} -> {c and d}")  # AND  
print(f"{c} or {d} -> {c or d}")    # OR  
print(f"not {d} -> {not d}")        # NOT  


# MEMBERSHIP OPERATORS  
print("\nMembership Operators")  
fruits = ["apple", "banana", "cherry"]  

print(f"'apple' in fruits -> {'apple' in fruits}")  
print(f"'grape' in fruits -> {'grape' in fruits}")  
print(f"'mango' not in fruits -> {'mango' not in fruits}")  
print(f"'cherry' in fruits -> {'cherry'in fruits}")
