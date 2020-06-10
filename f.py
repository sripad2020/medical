import time
import math
import random
f=[55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,76,77,79,80]
a1=input('enter the name: ')
a=float(input('enter your weight in kgs: '))
age=input('enter your age: ')
print('1 feet =12 inches')
print('1 inche=2.54 centimeters')
height=float(input('enter the height in centimeters: '))
print('NOW BREADTH ASSESMENT TAKE THE READIGS OF BREADTH FOR 1 MINUTE ')
print('MAINTAIN YOURSELF TO BE IN REST CONDITION ')
t=60
for i in range(t):
    print(t-i,'seconds are over ')
    time.sleep(1)
c=int(input('enter the breadth analaysis: '))
print('it should be between 12-20')
print('TAKE THE READINGS OF THE PULSE FOR 1 MINUTE ')
s=60
for i in range(s):
    print(s-i,'seconds are over ')
    time.sleep(1)
d=int(input('enter your pulse rate for 1 min: '))
print('it should be in between 60-100')
if age > '18':
    if c >20 and c<=12:
        print(a1,'is not safe ')
        print('he has low breadthing capacity.His brain is not getting correct amount of required oxygen')
    else:
        print('you are healthy')
    if d > 60 and d <100:
        print('not bad you are safe: ')
        t=random.choice(f)
        y=t*d
        print('amount of blood ejected from your heart per minute',y)
    else:
        print('You are in danger')
    if height > 0 and a > 0.0:
        bmi=a/(height * height)
        print(bmi*10000)
        if bmi > 18.5 or bmi < 24.5:
            print('you are safe ')
        else:
            print('you need more excersise ')
else:
    if c > 20 and c <= 12:
        print(a1, 'is not safe ')
        print('he has low breadthing capacity.His brain is not getting correct amount of required oxygen')
    else:
        print('you are healthy')
    if d > 60 and d < 100:
        print('not bad you are safe: ')
        t = random.choice(f)
        y = t * d
        print('amount of blood ejected from your heart per minute', y)
    else:
        print('You are in danger')
    if height > 0 and a > 0.0:
        bmi = a / (height * height)
        print(bmi * 10000)
    if bmi > 18.5 or bmi < 24.5:
        print('you are safe ')
    else:
        print('you need more excersise ')