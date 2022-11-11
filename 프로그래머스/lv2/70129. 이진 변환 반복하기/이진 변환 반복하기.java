class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int cnt=0;
        int zeroCnt=0;
        while(!s.equals("1")){
            zeroCnt+=s.length()-s.replace("0", "").length();
            s=s.replace("0", "");
            s=Integer.toBinaryString(s.length());
            cnt+=1;
        }
        answer[0]=cnt;
        answer[1]=zeroCnt;
        return answer;
    }
}