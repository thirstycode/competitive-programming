# Problem Sort (CodeChef)

Chef is organising a contest with P problems (numbered 1 through P). Each problem has S subtasks (numbered 1 through S).<br>

The difficulty of a problem can be calculated as follows:<br>

Let's denote the score of the k-th subtask of this problem by SCk and the number of contestants who solved it by NSk.<br>
Consider the subtasks sorted in the order of increasing score.<br>
Calculate the number n of valid indices k such that NSk>NSk+1.<br>
For problem i, the difficulty is a pair of integers (n,i).<br>
You should sort the problems in the increasing order of difficulty levels. Since difficulty level is a pair, problem a is more difficult than problem b if the number n is greater for problem a than for problem b, or if a>b and n is the same for problems a and b.<br>

### Input<br>
The first line of the input contains two space-separated integers P and S denoting the number of problems and the number of subtasks in each problem.<br>
2P lines follow. For each valid i, the 2i−1-th of these lines contains S space-separated integers SC1,SC2,…,SCS denoting the scores of the i-th problem's subtasks, and the 2i-th of these lines contains S space-separated integers NS1,NS2,…,NSS denoting the number of contestants who solved the i-th problem's subtasks.<br>
### Output<br>
Print P lines containing one integer each — the indices of the problems in the increasing order of difficulty.<br>

### Constraints<br>
1≤P≤100,000<br>
2≤S≤30<br>
1≤SCi≤100 for each valid i<br>
1≤NSi≤1,000 for each valid i<br>
in each problem, the scores of all subtasks are unique<br>
### Subtasks<br>
Subtask #1 (25 points): S=2<br>
Subtask #2 (75 points): original constraints<br>

#### Example Input<br>
3 3<br>
16 24 60<br>
498 861 589<br>
14 24 62<br>
72 557 819<br>
16 15 69<br>
435 779 232<br>
#### Example Output<br>
2<br>
1<br>
3<br>
