"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
read_question = open('question.txt', 'r')
question_list = [line.strip()for line in read_question]
read_question.close()
score = 0
total = len(question_list)
print(question_list)
for line in question_list:
    # split equation with `=` into question and answer
   q, a = line.split("=")
   ans = input(f'{q}=')

   if ans == a:
      score +=1

result = open("result.txt", 'w')
result.write(f'your final score is {score}/{total}')
result.close()
      

 