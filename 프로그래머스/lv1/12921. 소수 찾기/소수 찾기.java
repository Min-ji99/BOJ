class Solution {
    public int solution(int num){
        boolean prime[]=new boolean[num+1];
        prime[0]=prime[1]=true; //소수면 false, 소수가 아니면 true
        for(int i=2; i*i<=num; i++){
            if(!prime[i]){
                /*
                //i*i부터 i의 배수 다 소수에서 제거
                //i가 6일때 6*2, 6*3, 6*4, 6*5는 앞에서 2, 3, 4, 5의 배수 제거가 이미 되어있음
                for(int j=i*i; j<=num; j+=i) prime[j] = true;
                 */
                for(int j=i*2; j<=num; j+=i){
                    prime[j]=true;
                }
            }
        }
        int count=0;
        for(int i=2; i<=num; i++){
            if(!prime[i]) count+=1;
        }
        return count;
    }
}