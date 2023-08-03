# 1Mx1M Matching Challenge

### What?

* you have 2 lists of 1M elements
* each element is a 6 chars string (upercase, lowercase and numbers)
* you want to 
    * find the matching elements between lists
    * store the mathing elment, and the position in list1 and list2
* have fun writing as many different solutions as you -or a LLM- can came up with

### Scripts

#### [Double For Matching](https://github.com/huolter/1Mx1M-matching/blob/main/double_for_matching.py)
The worst possible scenario. This repo was inspired by the story of a programmer that took this approach to solve a similar problem. 
Two nested loops that lead to O(n^2) time. A real disaster. 
Running time in my AMD Ryzen 5 5500U w/ 16GB ram: NEVER ENDED XD

#### [Sets Intersection](https://github.com/huolter/1Mx1M-matching/blob/main/sets_intersection.py)
Transform the lists into sets and use intersection(). By converting the lists to sets and performing the intersection operation using sets, we reduce the complexity from O(n^2) to O(n), where n is the number of elements in each list. This will significantly improve the execution time for large datasets.
Execution time (same hardware): 2.81931734085083 seconds


#### [Hash and Match]()

The algorithmic approach used in the script is an efficient method to find matches between two large lists of elements. The main steps of the approach are as follows:

* Build a hash table for list1: The algorithm starts by iterating through list1 and building a hash table to store the elements and their corresponding positions in list1. The hash table is implemented as a Python dictionary, where the keys are the elements from list1, and the values are lists of positions where each element occurs.
* Find matches in list2: Next, the algorithm iterates through list2 and checks if each element exists in the hash table. If an element from list2 is found in the hash table, it means there's a match between the two lists. For each match, the algorithm retrieves the positions of the matching element in list1 and list2, creating a tuple containing the matching element and its positions.
* Accumulate matches: As the algorithm iterates through list2, it accumulates the matches in a list.

The key to the efficiency of this approach is the use of a hash table, which allows for constant-time lookups. By building the hash table for list1 once and then performing lookups for each element in list2, the algorithm reduces the overall time complexity to O(n), where n is the total number of elements in both lists.

Execution time: 1.234602928161621 seconds