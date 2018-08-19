# Sheokand and Number (CodeChef)
Sheokand is good at mathematics. One day, to test his math skills, Kaali gave him an integer N. To impress Kaali, Sheokand has to convert N into an integer M that can be represented in the form 2x+2y (where x and y are non-negative integers such that x≠y). In order to do that, he can perform two types of operations:<br>

add 1 to N<br>
subtract 1 from N<br>
However, Sheokand is preparing for his exams. Can you help him find the minimum number of operations required to convert N into a valid integer M?<br>

Input<br>
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.<br>
The first and only line of each testcase contains a single integer N.<br>
Output<br>
For each test case, print a single line containing one integer — the minimum required number of operations.<br>

Constraints<br>
1≤T≤100,000<br>
1≤N≤109<br>
Subtasks<br>
Subtask #1 (30 points): 1≤T≤1,000<br>
Subtask #2 (70 points): original constraints<br>

Example Input<br>
3<br>
10<br>
22<br>
4<br>
Example Output<br>
0<br>
2<br>
1<br>
Explanation<br>
Example case 1: N=10 is already in the form 2x+2y, with x=3 and y=1.<br>

Example case 2: N=22 can be converted into M=20=22+24 or M=24=23+24 in two operations.<br>

Example case 3: N=4 can be converted into M=3=20+21 or M=5=20+22 in one operation.<br>

