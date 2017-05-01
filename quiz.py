from random import shuffle


print('Welcome to the wonderful quiz on economics!')
print('This quiz will involve simple economics questions')

qas = [
    ('Question', 'Economics'),
    ('Question', 'Economics'),
    ('Question', 'Economics'),
    ('Question', 'Economics'),
    ('Question', 'Economics'),
   
   
]
shuffle(qas)
numRight = 0
wrong = []

numQuestions = int(input("How many questions? "))

for question, rightAnswer in qas[:numQuestions]:
    answer = input(question + ' ')
    if answer.lower() == rightAnswer:
        print('Right!')
        numRight += 1
    else:
        print('No, the answer is %s' % rightAnswer)
        wrong.append(question)

print('You got %d right and the following wrong:' % (numRight))
for q in wrong:
    print(q)
