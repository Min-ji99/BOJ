import java.util.ArrayList;
import java.util.List;

class Solution {
     public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List<Integer> answerList=new ArrayList<>();

        int beforeTime=(int)Math.ceil((double)(100-progresses[0])/(double)speeds[0]);
        int cnt=1;
        for(int i=1; i<progresses.length; i++){
            int time=(int)Math.ceil((double)(100-progresses[i])/(double)speeds[i]);

            if(beforeTime>=time){
                cnt++;
            }else{
                answerList.add(cnt);
                cnt=1;
                beforeTime=time;
            }
        }
        answerList.add(cnt);
        
        answer=new int[answerList.size()];
        for(int i=0; i<answer.length; i++){
            answer[i]=answerList.get(i);
        }
        return answer;
    }
}