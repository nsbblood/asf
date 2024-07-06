print('hi')
print('Hello','Malatya') #Add your reviews like this :)

other_print=print
other_print('Lets test this too!') #We gave print function to other_print 

machine_print=print
machine_print('I am machine print! Lets print them all')
# This time we gave print function to machine_print. Now machine_print
#can print like print function

#num1= 8
#num2= 5
#result= num1*num2
#result= result+10
#result= result/1.5
#result= result-num1
#print(result)
#It goes step by step as expected


def do_math(num1, num2): # dont forget to use : at functions like this 
    result= num1*num2
    result= result+10
    result= result/1.5
    result= result-num1
    return result

print(do_math(5,3))
print(do_math(44,3))
a=5
b=4
print(do_math(a,b))

