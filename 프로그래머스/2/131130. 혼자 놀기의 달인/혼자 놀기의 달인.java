import java.util.*;

class Solution {
    public int solution(int[] cards) {
        int answer = 0;
        int n = cards.length;
        
        List<Integer> scores = new ArrayList<>();
        int[] open = new int[n]; //0 : 오픈X, 1: 오픈O
        for(int i=0; i<n; i++) {
            int score1 = 0;
            int idx=i;
            while(true) {
                if(open[idx]==0) {
                    score1 ++;
                    open[idx]=1;
                    idx = cards[idx]-1;
                }else{
                    break;
                }
            }
            scores.add(score1);
        }
        
        System.out.println(scores.toString());
        
        int scoreCnt = scores.size();
        if(scoreCnt == 1) return 0;
        
        Collections.sort(scores);
        
        answer = scores.get(scoreCnt-1)*scores.get(scoreCnt-2);
        
        return answer;
    }
}