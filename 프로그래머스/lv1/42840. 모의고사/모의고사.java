import java.util.*;

class Solution {
    public int calcScore(int[] answers, int[] pettern){
        int score=0;
        
        for(int i=0; i<answers.length; i++){
            if(answers[i]==pettern[i%pettern.length]){
                score+=1;
            }
        }
        return score;
    }
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[][] pettern={{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        Solution solution=new Solution();
        int[] score=new int[3];
        for(int i=0; i<pettern.length; i++){
            score[i]=solution.calcScore(answer, pettern[i]);
        }
        int[] scores=new int[3];
        int maxScore=0; //최대 점수
        for(int i=0; i<pettern.length; i++){
            scores[i]= solution.calcScore(answers, pettern[i]); //점수 계산
            if(maxScore<scores[i]){
                maxScore=scores[i];
            }
        }
        List<Integer> list=new ArrayList<>();
        for(int i=0; i<scores.length; i++){
            if(maxScore==scores[i]){
                list.add(i+1);
            }
        }
        answer=new int[list.size()];
        for(int i=0; i<answer.length; i++){
            answer[i]=list.get(i);
        }
        return answer;
    }
}