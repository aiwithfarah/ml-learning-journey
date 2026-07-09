# tuple of 5 quetions
# 2D Tuple of options
# tuple of answers 
# list of guesses
# total score variable
# variable to keep track of what num question we are on

questions = ("What is the capital of France?",
             "How many planets are in our solar system?",
             "Which is the largest ocean on Earth?",
             "What color do you get when you mix blue and yellow paint?",
             "Which gas do humans need to breathe in to survive?")

options = (
    ("A. Rome", "B. London", "C. Berlin", "D. Paris"),
    ("A. 6","B. 7","C. 8","D. 9"),
    ("A. Arctic", "B. Pacific", "C. Atlantic", "D. Indian"),
    ("A. Green", "B. Orange", "C. Brown", "D. Purple"),
    ("A. Nitrogen", "B. Oxygen", "C. Hydrogen", "D. Co2")
    )

answers = ("D", "C", "B", "A", "B")

guesses = []

total_score = 0

question_num = 0

count = 0

# display question
for question in  questions:
    print("----------------")
    print(question)
    # display options
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess: ['A', 'B', 'C', 'D'] - ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        count += 1
        total_score += 1
        print("Correct")
    else:
        print(f"Incorrect {answers[question_num]} is the correct answer!")

    question_num += 1

print("-------")
print("Results")
print("-------")

print("ANSWERS: ", end="")
for answer in answers:
    print(answer, end=' | ')
print()

print("GUESSES: ", end="")
for guess in guesses:
    print(guess, end=" | ")
print()
print(f"You has answered {count} questions correctly.\nYour Score : {int(total_score/len(questions) * 100)}")