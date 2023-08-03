#1Mx1M Matching Challenge

### What?

* you have 2 lists of 1M elements
* each element is a 6 chars string (upercase, lowercase and numbers)
* you want to 
** find the matching elements between lists
** store the mathing elment, and the position in list1 and list2
* have fun writing as many different solutions as you -or a LLM- can came up with

### Scripts

## Double For Matching
The worst possible scenario. This repo was inspired by the story of a programmer that took this approach to solve a similar problem. 
Two nested loops that lead to O(n^2) time. A real disaster. 
Running time in my AMD Ryzen 5 5500U w/ 16GB ram: NEVER ENDED XD