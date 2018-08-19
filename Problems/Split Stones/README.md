There are three piles of stones. The first pile contains a stones, the second pile contains b stones and the third pile contains c stones. You must choose one of the piles and split the stones from it to the other two piles; specifically, if the chosen pile initially contained s stones, you should choose an integer k (0≤k≤s), move k stones from the chosen pile onto one of the remaining two piles and s−k stones onto the other remaining pile. Determine if it is possible for the two remaining piles (in any order) to contain x stones and y stones respectively after performing this action.<br>

Input<br>
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.<br>
The first and only line of each test case contains five space-separated integers a, b, c, x and y.<br>
Output<br>
For each test case, print a single line containing the string "YES" if it is possible to obtain piles of the given sizes or "NO" if it is impossible.<br>

Constraints<br>
1≤T≤100<br>
1≤a,b,c,x,y≤109<br>
Subtasks<br>
Subtask #1 (20 points): 1≤a,b,c,x,y≤100<br>
Subtask #2 (80 points): original constraints<br>

Example Input<br>
4<br>
1 2 3 2 4<br>
3 2 5 6 5<br>
2 4 2 6 2<br>
6 5 2 12 1<br>
Example Output<br>
YES<br>
NO<br>
YES<br>
NO<br>
Explanation<br>
Example case 1: You can take the two stones on the second pile, put one of them on the first pile and the other one on the third pile.<br>

Example case 2: You do not have enough stones.<br>

Example case 3: You can choose the first pile and put all stones from it on the second pile.<br>
