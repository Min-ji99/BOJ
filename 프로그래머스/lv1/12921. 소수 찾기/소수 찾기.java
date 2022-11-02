class Solution {
    public int solution(int num){
        boolean prime[]=new boolean[num+1];
        prime[0]=prime[1]=true; //소수가 아니면 true
        for(int i=2; i*i<=num; i++){
            if(!prime[i]){
                // prime[j] 소수가 아닌 표시
                for(int j=i*2; j<=num; j+=i) prime[j] = true;
            }
        }
        int count=0;
        for(int i=2; i<=num; i++){
            if(!prime[i]) count+=1;
        }
        return count;
    }
}