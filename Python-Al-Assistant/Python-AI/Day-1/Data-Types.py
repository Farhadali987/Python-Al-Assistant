# Integer (Age of a person)
age = 25
print("Age:", age)
print("Type:", type(age))

# Float (Height in meters)
height = 5.9
print("Height:", height, "meters")
print("Type:", type(height))

# String (Full Name)
full_name = "Farhad Gul"
print("Full Name:", full_name.upper())  # Convert to uppercase
print("Type:", type(full_name))

# Boolean (Is student?)
is_student = True
print("Is Student?", is_student)
print("Type:", type(is_student))

# List (Shopping Items)
shopping_list = ["Milk", "Eggs", "Bread", "Butter"]
shopping_list.append("Cheese")  # Add an item
print("Shopping List:", shopping_list)
print("Type:", type(shopping_list))

# Tuple (Coordinates of a location)
location_coordinates = (24.8607, 67.0011)  # Latitude, Longitude
print("Location Coordinates:", location_coordinates)
print("Type:", type(location_coordinates))

# Set (Unique phone numbers)
unique_numbers = {12345, 67890, 12345, 54321}
unique_numbers.add(99999)  # Adding new number
print("Unique Phone Numbers:", unique_numbers)  # Removes duplicates
print("Type:", type(unique_numbers))

# Dictionary (Student details)
student_details = {
    "Name": "Farhad Ali",
    "Roll No": 108,
    "Subjects": ["Math", "Science", "English"]
}
print("Student Details:", student_details)
print("Type:", type(student_details))

# None Type (Represents no value)
user_response = None
print("User Response:", user_response)
print("Type:", type(user_response))

# Bytes (Secret message)
secret_msg = b"Hello!"
print("Secret Message:", secret_msg)
print("Type:", type(secret_msg))

# Bytearray (Editable byte sequence)
mod_bytes = bytearray([100, 110, 120])
mod_bytes[0] = 105  # Modifying first value
print("Modified Bytes:", mod_bytes)
print("Type:", type(mod_bytes))

# Range (Numbers from 1 to 10)
numbers = range(1, 11)  # 1 to 10
print("Numbers:", list(numbers))
print("Type:", type(numbers))

# Frozen Set (Immutable group of subjects)
subjects = frozenset(["Math", "Science", "English"])
print("Subjects (Immutable):", subjects)
print("Type:", type(subjects))
