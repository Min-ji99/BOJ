class Solution {
    public int divisorCnt(int num){
        int cnt=0;
        for(int i=1; i*i<=num; i++){
            if(i*i==num) {
                cnt++;
                continue;
            }
            if(num%i==0) {
                cnt+=2;
            }
        }
        return cnt;
    }
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        for(int i=1; i<=number; i++){
            int attack=divisorCnt(i);
            if(attack>limit) answer+=power;
            else answer+=attack;
        }
        
        return answer;
    }
}