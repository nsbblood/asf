def num_sum(num1,num2):
    #try:
    #    print(num1+num2)
    #except Exception:
    #    print('There was an error. You wrote: ')
    if type(num1)!=int or type(num2)!=int:
        raise Exception('You should use integars')

    print(num1+num2)

num_sum(1,5)
try:
 num_sum(1,'hi')
except Exception as e:
   print(f'Something went wrong: {e}')
   
num_sum(4,5)
num_sum(2,5)
