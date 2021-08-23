print("Hello, welcome to the Quiz!")

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 2

if ans.lower() == 'yes':
    ans = input('1. What is 1+1?')
    if ans == '2':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


    ans = input('2. What is the best programming language?')
    if ans.lower() == 'python':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

print('Thank you for playing ', score, 'questions correct.')
mark = (score/total_q)*100
print('Mark:', mark, '%')
print('Goodbye!')
