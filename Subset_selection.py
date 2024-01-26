#Mini Project-1  ------->subset-selection part-1
from itertools import combinations #importing the lirary and it's function combination

nums = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]   #Data on which program is to be fitted

#use of function 'combination' to prepare subsets of size 5 with sum of number inside is zero
subsets = [subset for subset in combinations(nums, 5) if sum(subset) == 0]  

for subset in subsets:
    print(subset , end=' \n')    #Prints all the subsets 
print ("\nTotal Sets: ", len(subsets), "\n")   #Prints the total subsets formed



#subset-selection part-2
from itertools import combinations #importing the lirary and it's function combination

nums = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]  #Data on which program is to be fitted

#'combination' function prepare subsets of size 3 to 6 only with sum of numbers inside is zero
subsets = [subset for r in range(3, 7) for subset in combinations(nums, r) if sum(subset) == 0]

for subset in subsets:
    print(subset)   #prints all the subsets formed
print ("\nTotal Sets: ", len(subsets), "\n")  #prints the total sets formed

