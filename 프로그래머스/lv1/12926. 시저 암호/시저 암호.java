class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == ' ') {
                answer += s.charAt(i);
                continue;
            }
            if (ch >= 'a' && ch <= 'z') {
                answer+=(char)((ch+n-'a')%26+'a');
            }else if(ch>='A' && ch<='Z'){
                answer+=(char)((ch+n-'A')%26+'A');
            }
        }

        return answer;
    }
}