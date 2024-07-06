def fuzzy_math(num1,operator,num2):
    if type(num1) !=int or type(num2) !=int:
        raise Exception('We need to focus on here more!')
    
    if operator == '+':
        result= num1+num2
    elif operator == '*':
        result=num1*num2
    else:
        raise Exception(f"I dont know how to do math with '{operator}'")
    
    if result <0:
        return 'Whaaat a negative number ??'
    elif result< 10:
        return 'samll number, I can deal with that'
    elif result< 20:
        return ' A medium sized number'
    else:
        return ' A bid number you ...'
    
    
class TestFuzzymath:
        def test_non_int_input_for_num1(self):
            pass

        def test_non_int_input_for_num2(self):
            pass
        
        def test_addition_with_negatif_result(self):

            pass

        def test_addition_with_small_result(self):
            assert fuzzy_math(2,'+',2)=='A small number, I can deal with that'

        def test_addition_with_medium_result(self):
            pass

        def test_addition_with_large_result(self):
            pass

        def test_multiplication_with_negatif_result(self):

            pass

        def test_multiplication_with_small_result(self):
            pass

        def test_multiplication_with_medium_result(self):
            pass

        def test_multiplication_with_large_result(self):
            pass

        def test_invalid_operator(self):
            pass



