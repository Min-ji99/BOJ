class Solution {
    public boolean isPrime(int n){
        if(n==2) return true;
        for(int i=2; i<Math.sqrt(n)+1; i++){
            if(n%i==0) return false;
        }
        return true;

    }
    public int solution(int n) {
        int answer = 0;
        Solution findPrime=new Solution();
        for(int i=2; i<=n; i++){
            if(isPrime(i)) {
                answer+=1;
            }
        }
        return answer;
    }
}