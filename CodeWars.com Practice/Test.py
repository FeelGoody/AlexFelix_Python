from copy import deepcopy

test_tuple = [['a', 'b', 'c'], 3, 5, 1, 5]
new_tuple = deepcopy(test_tuple)
test_tuple[0].append('d')
test_tuple.append(15)

print('new_tuple:', new_tuple)
print('test_tuple:', test_tuple)


# [['a', 'b', 'c'], 3, 5, 1, 5]