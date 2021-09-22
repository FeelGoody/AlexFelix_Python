# https://www.codewars.com/kata/60dda5a66c4cf90026256b75
# import codewars_test as test
# from solution import some_but_not_all

# @test.describe("Basic Examples")
# def test_group():
#     @test.it("Basic Test Cases")
#     def test_case():
#         test.assert_equals(some_but_not_all('abcdefg&%$', str.isalpha), True)
#         test.assert_equals(some_but_not_all('&%$=', str.isalpha), False)
#         test.assert_equals(some_but_not_all('abcdefg', str.isalpha), False)
#         test.assert_equals(some_but_not_all([4, 1], lambda x: x>3), True)
#         test.assert_equals(some_but_not_all([1, 1], lambda x: x>3), False)
#         test.assert_equals(some_but_not_all([4, 4], lambda x: x>3), False)



def some_but_not_all(seq, pred):

    indTrue = 0
    for value in seq:
        if pred(value):
            indTrue += 1

    if indTrue == 0 or indTrue == len(seq):
        return False
    else:
        return True


def if_even(num):
    if num % 2 == 0:
        return True
    else: return False

pred = if_even
print(pred)
print(pred(5))

# some_but_not_all('Mon%_Tue_Wed', str.isalpha)
# some_but_not_all([4, 4], lambda x: x > 3)
# some_but_not_all('abcdefg&%$', str.isalpha)
from_func = some_but_not_all([4,4,765,234], if_even)
print(from_func)
