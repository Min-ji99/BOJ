class Solution {
        public int sumOfDigits(int x){
        int sum=0;
        while(x>0){
            sum+=x%10;
            x/=10;
        }
        return sum;
    }
    public boolean checkRemainder(int x, int sum){
        if(x%sum==0){
            return true;
        }
        return false;
    }
    public boolean solution(int x) {
        boolean answer = true;
        int sum=sumOfDigits(x);
        answer=checkRemainder(x, sum);
        return answer;
    }
}