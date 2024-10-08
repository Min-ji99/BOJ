import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        int diff = (int)right-(int)left;
        int[] answer = new int[diff+1];
        
        int idx = 0;
        while(left<=right) {
            long i = left/n;
            long j = left%n;
            
            answer[idx] = Math.max((int)i, (int)j)+1;
            idx++;
            left++;
        }
        
        return answer;
    }
}


/*
n = 3 left 2 right 5
1 2 3 
2 2 3
3 3 3

[1, 2, 3, 2, 2, 3, 3, 3, 3]

1차원 배열일때 2차원 배열 위치 : [idx/n][idx%n]
left = 2 : [0, 2]
right = 5 : [1, 2]

제일 큰 행 or 열 영향
i<j : j+1
i>j : i+1
i=j : i

4x4
1, 2, 3, 4
2, 2, 3, 4
3, 3, 3, 4
4, 4, 4, 4

*/

