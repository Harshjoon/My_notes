# Combination and permuations

# Combination is ways in which you can group in which order does not mathher.
# Permutaion is ways in which you can group in whcih order does matter.

###################################################
'''Example 1'''
# import itertools
# my_list = [1,2,3]

# combinations = itertools.combinations(my_list,3)
# for c in combinations:
#     print(c)

# combinations = itertools.combinations(my_list,2)
# for c in combinations:
#     print(c)

# permutations = itertools.permutations(my_list,3)
# for c in permutations:
#     print(c)

###################################################
'''Example 2'''
# import itertools
# my_list = [1,2,3,4,5,6]

# combinations = itertools.combinations(my_list, 3)
# permuations  = itertools.permutations(my_list, 3)

# print( [ x for x in combinations if sum(x) == 10 ] )
# print( [ x for x in permuations if sum(x) == 10 ] )

###################################################
'''Example 3'''
import itertools

word        = 'sample'
my_letters  = 'plmeas'

combinations  = itertools.combinations(my_letters, 6)
permutations  = itertools.permutations(my_letters, 6)

for p in permutations:
    print(p)
    if ''.join(p) == word:
        print("Match!")
        break
else:
    print("no match")
