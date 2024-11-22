# Test results: True indicates correct, False indicates incorrect
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# Calculate the number of test questions
num_questions = len(test_results)

# Calculate the number of correct answers
correct_answers = 0
for answer in test_results:
   if answer:  # True means correct
      correct_answers += 1

# Calculate the number of incorrect answers
incorrect_answers = num_questions - correct_answers

# Calculate the percentage of correct answers
percentage_correct = (correct_answers / num_questions) * 100

# Display the results
print('TEST STATISTICS')
print('===============')
print('Number of questions:', num_questions)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers: {:.2f}%'.format(percentage_correct))