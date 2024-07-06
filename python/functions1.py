import random #import random yaparak randomu çağırmış oldum

def Do_math(num1, num2): #def i büyük harfle başlattım diye kıyamet koptu 
    result= num1*num2
    result= result+10
    result = result*4
    return result

a= random.randint(1,44) #random.randint ile rastgele değerler atadık
b= random.randint(1,5)
print('The result:',Do_math(a,b))

# lets import operator
import operator
print(operator.add(2,2))
print(operator.not_(False))


def other_function(arg=1,arg2='a',arg3=None,arg4=True,arg5='Hello'):
    pass
     
other_function(1,arg4=False)
