import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        Arrays.sort(jobs, (o1, o2)->o1[0]-o2[0]);

        PriorityQueue<int[]> priorityQueue=new PriorityQueue<>((o1, o2)->o1[1]-o2[1]); //작업이 빨리 끝나는 작업이 우선순위가 높음
        int time=0;
        int count=0;
        int idx=0;
        while(count<jobs.length) {
            while(idx< jobs.length && jobs[idx][0]<=time){
                priorityQueue.add(jobs[idx++]);
            }
            if(!priorityQueue.isEmpty()) {
                int[] job = priorityQueue.poll();
                answer += time - job[0] + job[1];
                time += job[1];
                count++;
            }else{
                time=jobs[idx][0];
            }
        }
        return (int)Math.floor(answer/jobs.length);
    }
}