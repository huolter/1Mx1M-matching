# 1Mx1M Matching Challenge

## What?

* you have 2 lists of 1M elements (generated with [this script](https://github.com/huolter/1Mx1M-matching/blob/main/generator.py))
* each element is a 6 chars string (upercase, lowercase and numbers)
* you want to: 
    * find the matching elements between lists
    * store the matching elment and the position the element has in both original lists
* have fun :-)

## Why?

Some days ago we -wife and I- had lunch with a friend and he told us the story of a programmer at his job that tried to solve a similar problem using a poor perfoming approach, something like the nested for loops. I kept thinking about this and decided to collect different solutions. 

## Scripts

### [Double For Matching](https://github.com/huolter/1Mx1M-matching/blob/main/double_for_matching.py)
The worst possible scenario. This repo was inspired by the story of a programmer that took this approach to solve a similar problem. 
Two nested loops that lead to O(n^2) time. A real disaster. 

**Running time in my AMD Ryzen 5 5500U w/ 16GB ram: NEVER ENDED XD**

### [Sets Intersection](https://github.com/huolter/1Mx1M-matching/blob/main/sets_intersection.py)
Transform the lists into sets and use intersection(). By converting the lists to sets and performing the intersection operation using sets, we reduce the complexity from O(n^2) to O(n), where n is the number of elements in each list. This will significantly improve the execution time for large datasets.

**Execution time (same hardware): 2.81931734085083 seconds**


### [Hash and Match](https://github.com/huolter/1Mx1M-matching/blob/main/hash_and_match.py)

The algorithmic approach used in the script is an efficient method to find matches between two large lists of elements. The main steps of the approach are as follows:

* Build a hash table for list1: The algorithm starts by iterating through list1 and building a hash table to store the elements and their corresponding positions in list1. The hash table is implemented as a Python dictionary, where the keys are the elements from list1, and the values are lists of positions where each element occurs.
* Find matches in list2: Next, the algorithm iterates through list2 and checks if each element exists in the hash table. If an element from list2 is found in the hash table, it means there's a match between the two lists. For each match, the algorithm retrieves the positions of the matching element in list1 and list2, creating a tuple containing the matching element and its positions.
* Accumulate matches: As the algorithm iterates through list2, it accumulates the matches in a list.

The key to the efficiency of this approach is the use of a hash table, which allows for constant-time lookups. By building the hash table for list1 once and then performing lookups for each element in list2, the algorithm reduces the overall time complexity to O(n), where n is the total number of elements in both lists.

**Execution time: 1.234602928161621 seconds**

### [Sets Comprehension](https://github.com/huolter/1Mx1M-matching/blob/main/sets_comprehension.py)

This solution still utilizes sets to find common elements between the two lists, but instead of building a hash table, it directly finds the positions of matching elements using list comprehensions. The code is more concise and efficient since it doesn't store all the intermediate positions in separate lists. Instead, it directly extends the matches list with tuples containing the element and its positions in list1 and list2.

The use of sets ensures faster lookups when finding common elements, and the overall time complexity of the solution remains O(n), where n is the total number of elements in both lists.

**Execution time: 2.7240407466888428 seconds**

### [Numpy Where](https://github.com/huolter/1Mx1M-matching/blob/main/numpy_where.py)

In this version, we use NumPy's array operations to find the positions of matching elements. The np.where() function returns the indices of elements that satisfy the condition, and we use this to find the positions of the matching elements in both lists.

**Execution time: 8.953785181045532 seconds**

### [Pandas Merge](https://github.com/huolter/1Mx1M-matching/blob/main/pandas_merge.py)

In this solution, we use pandas to convert both lists (list1 and list2) into data frames (df1 and df2). We then perform an inner [merge operation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) between the data frames based on the common elements between the two lists. The result of the merge is a new data frame containing the matching elements and their positions in both lists.

Finally, we convert the resulting data frame to a list of tuples (matches_list), containing the matching element and its positions, which is the desired output.

**Execution time: 1.3652698993682861 seconds**

### [Dask Bags](https://github.com/huolter/1Mx1M-matching/blob/main/dask_bags.py)

In this version, we use [Dask.bag](https://docs.dask.org/en/stable/bag.html) to create distributed bags from the input lists. The db.from_sequence() function parallelizes the creation of the bags, allowing for better scalability with larger datasets.

The common elements are found using the set intersection operation between the two bags. After that, the code proceeds to find the positions of matching elements in both lists, similar to the previous versions.

Dask can efficiently handle large datasets and parallelize operations across multiple cores, making it a powerful choice for performance-critical tasks.

**Execution time: 5.9499101638793945 seconds**

### [Pandarallel](https://github.com/huolter/1Mx1M-matching/blob/main/pandarallel_pandas.py)

In this solution, we use the [pandarallel](https://pypi.org/project/pandarallel/) library along with pandas to enable parallel processing. The pandarallel library allows pandas to perform operations in parallel across multiple CPU cores.

We convert list1 and list2 into pandas data frames (df1 and df2) and perform an inner merge operation based on the common elements between the two data frames. The result of the merge is a new data frame (common_elements) containing the matching elements and their positions in both lists.

**Execution time: 1.60727858543396 seconds**