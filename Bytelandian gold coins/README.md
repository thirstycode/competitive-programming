All submissions for this problem are available.<br>
In Byteland they have a very strange monetary system.<br>

Each Bytelandian gold coin has an integer number written on it. A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. But these numbers are all rounded down (the banks have to make a profit).<br>

You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins.<br>

You have one gold coin. What is the maximum amount of American dollars you can get for it?<br>

Input<br>
The input will contain several test cases (not more than 10). Each testcase is a single line with a number n, 0 <= n <= 1 000 000 000. It is the number written on your coin.<br>

Output<br>
For each test case output a single line, containing the maximum amount of American dollars you can make.<br>
<br>
Example<br>
Input:<br>
12<br>
2<br>
<br>
Output:<br>
13<br>
2<br>
You can change 12 into 6, 4 and 3, and then change these into 6+4+3=13. If you try changing the coin 2 into 3 smaller coins, you will get 1, 0 and 0, and later you can get no more than 1outofthem.Itisbetterjusttochangethe2coindirectlyinto2.<br>
