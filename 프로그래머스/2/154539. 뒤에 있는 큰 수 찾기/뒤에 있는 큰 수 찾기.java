import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int len = numbers.length;

        int[] answer = new int[len];
        
        //numbers의 인덱스 값 추가
        Stack<Integer> stack = new Stack<>();
        
        for(int i=0; i<len; i++) {
            if(stack.isEmpty()) {
                stack.push(i);
                continue;
            }
            
            //스택 맨 위의 값이랑 비교
            while(!stack.isEmpty() && numbers[stack.peek()]<numbers[i]) {
                answer[stack.pop()] = numbers[i];
            }
            stack.push(i);
        }
        
        while(!stack.isEmpty()) {
            int idx = stack.pop();
            answer[idx] = -1;
        }
        
        
        return answer;
    }
}

/*
바로 뒤에 큰수를 어케 찾지,,,,


numbers[4] = 6 스택 아래에 있는 값보다 크니까 
numbers[0] = 9 

numbers[2]가 스택으로 들어왔을 때,
스택 아래(numbers[1])에 있는 값보다 크니까 result[1]= numbers[2] = 5

numbers[4]가 스택으로 들어왔을 때,
스택 아래(numbers[3])에 있는 값보다 크니까 result[3] = numbers[4] = 6

numbers[3] 삭제 후
스택 아래(numbers[2])에 있는 값보다 크니까 result[2] = numbers[4] = 6
*/