import java.util.*;

public class Solution {
    public int[] solution(int[] arr){
        Stack<Integer> stack=new Stack<>();
        stack.add(arr[0]);
        for(int i=0; i<arr.length; i++){
            if(stack.peek()!=arr[i]){
                stack.add(arr[i]);
            }
        }
        int[] answer=new int[stack.size()];
        for(int i=0; i<answer.length; i++){
            answer[i]=stack.get(i);
        }
        return answer;
    }
}