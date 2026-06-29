# General Knowledge Quiz

score = 0

print("===== Welcome to the General Knowledge Quiz =====\n")

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()
if answer == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# Question 3
answer = input("3. Who wrote 'Romeo and Juliet'? ").strip().lower()
if answer == "william shakespeare" or answer == "shakespeare":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is William Shakespeare.\n")

# Question 4
answer = input("4. What is the largest ocean on Earth? ").strip().lower()
if answer == "pacific ocean" or answer == "pacific":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Pacific Ocean.\n")

# Question 5
answer = input("5. How many days are there in a leap year? ").strip().lower()
if answer == "366":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 366.\n")

print("===== Quiz Finished =====")
print(f"Your Score: {score}/5")

if score == 5:
    print("Excellent! Perfect score!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing and try again!")