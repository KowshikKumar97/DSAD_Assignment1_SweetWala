# Hyderabad_SweetWala

# Problem Statement
In Hyderabad City, there is a sweet shop called Sweetwala. That Shop manager wants to prepare an assorted sweet box. In shop there are N types of sweets are available. In each sweet box manger wants to put M items. Each item's cost is cost[i] and the delivery charge is delivery_cost[i], where i = 0 to N. Now condition is that Shop manager wants to select exactly M items in a such way that the total cost should be maximised.
The total cost of  an assorted box = The sum of costs of selected M items + (minimum delivery cost among M items * total no. of items (M)).
Help the shop manager find the maximum cost for M items in that assorted box.

# Requirements

1.	Read the input from a file(inputPS9.txt).
2.	You will output your answers to a file (outputPS9.txt) for each line.
3.	Perform an analysis for the features above and give the running time in terms of input size: n.

# Input Format:

The first line T denoting the number of test cases. The description of T test cases is as follows.

•	The first line of each test case contains two integers N and M separated with space.
•	The second line of each test case contains N integers where the ith integer indicates the cost[i].
•	The third line of each test case contains N integers where the ith integer denotes the delivery_cost[i].

# Sample Input:

1
5 3
8 7 2 6 10
1 5 8 4 8


# Output Format:

For each testcase, display a maximum possible cost for M items.

35

Note that the input/output data shown here is only for understanding and testing, the actual file used for evaluation will be different.


# Explanation:

Sweets 2, 4, and 5 could be put in the assorted box. The total cost = (7 + 6 + 10) + (min(4, 5, 8) * 3))
= 35
