def array_diff(a, b):
    # num1 = len(a)
    # num2 = len(b)
 
  empty_List = []
  list1 = [[8,1], 7 ,3 ,4]
  testList = [i[0] for i in list1 if type(i) == list]
  print(testList)
  # for index, i in enumerate(a):      
  #   if not i in b:
  #     empty_List.append(i)
  # return empty_List


ret = array_diff([1,5,2], [6,5,6,8])
print(ret)
        # test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.
