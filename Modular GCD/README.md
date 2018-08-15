# Modular GCD (CodeChef)


Given integers A, B and N, you should calculate the GCD of A^N+B^N and |A−B|. (Assume that GCD(0,a)=a for any positive integer a). Since this number could be very large, compute it modulo 1000000007 (109+7).<br>

#### Input<br>
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.<br>
The first and only line of each test case contains three space-separated integers A, B and N.<br>
Output<br>
For each test case, print a single line containing one integer — the required GCD modulo 109+7.<br>

#### Constraints<br>
1≤T≤10<br>
1≤A,B,N≤1012<br>
B≤A<br>
#### Subtasks<br>
Subtask #1 (10 points): 1≤A,B,N≤10<br>
Subtask #2 (40 points): 1≤A,B,N≤109<br>
Subtask #3 (50 points): original constraints<br>

#### Example Input<br>
2<br>
10 1 1<br>
9 1 5<br>
#### Example Output<br>
1<br>
2<br>
#### Explanation<br>
Example case 1: GCD(101+11,10−1)=GCD(11,9)=1<br>
Example case 2: GCD(95+15,9−1)=GCD(59050,8)=2<br>
