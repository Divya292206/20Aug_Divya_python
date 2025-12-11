import random

x = random.random() #0.0 to 1.0
print(x)

x = random.randint(1,100) #1 to 100
print(x)

list1 = [10,20,30,40,50,60,70,80,90]
x = random.choice(list1) #random value from list
print(x)

captcha = ["gy6dch","3ekjfe7","ncj87df","bsjd93","xnsj82","dc73jd","sdjsd44r","sdnsj8e","snjn4","dcnj83"]
x = random.choice(captcha)
print("Captcha is :",x)

random.shuffle(list1) #shuffle the list
print(list1)

x = random.sample(list1,3) #3 random value from list
print(x)