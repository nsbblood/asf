import random

if True:
    print('true!')

else:
    print('false')


a=random.randint(1,10)

if a==5:
    print('a is 5')

elif a==6:
    print('a is 6')

elif a==7:
    print('a is 7')

else:
    print('a is not found')


for letter in ['1','2','3','4','5']:
    print(letter.upper())

#for letter_2 in ['z','x','f','k','r']:
   # print(letter_2.upper())

for namelist in ['elisa','enes','ayse','hamburg','Malatya','Bursa']:
    print(namelist.upper())
