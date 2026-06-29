import random
import string

print("===== Random Password Generator =====")

# Get password length from the user
length = int(input("Enter password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits

# Generate the password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the result
print("\nGenerated Password:")
print(password)