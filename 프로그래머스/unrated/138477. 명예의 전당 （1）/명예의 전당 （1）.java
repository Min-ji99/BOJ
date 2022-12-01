/*
list로 명예전당에 오르는 점수를 관리한다
list의 최소값을 출력
1. k일차까지는 list에 추가하고 최솟값 출력
2. 이후부터는 list의 최솟값보다 크면 list의 최솟값을 대신 비교하던 score로 변경
*/
import java.util.Arrays;

class Solution {
    public int findmin(int[] fame){
        int min_idx=0;
        for(int i=0; i<fame.length; i++){
            if(fame[min_idx]>fame[i]) min_idx=i;
        }
        return min_idx;
    }
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        int[] fame=new int[k];
        int min_idx=0;
        for(int i=0; i<score.length; i++){
            if (i < k) {
                fame[i]=score[i];
                if(score[min_idx]>score[i]) min_idx=i;
                answer[i]=fame[min_idx];
                //System.out.println("answer" + Arrays.toString(answer));
            }else{
                if(fame[min_idx]<score[i]) {
                    fame[min_idx] = score[i];
                    min_idx=findmin(fame);
                }
                answer[i]=fame[min_idx];
                //System.out.println("answer" + Arrays.toString(answer));
            }
        }
        return answer;
    }
}