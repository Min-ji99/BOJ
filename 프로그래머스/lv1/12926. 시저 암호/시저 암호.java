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
                if (ch + n > 'z') {
                    answer += (char) (ch + n - 26);
                }else {
                    answer+=(char)(ch+n);
                }
            }else if(ch>='A' && ch<='Z'){
                if(ch+n>'Z'){
                    answer+=(char)(ch+n-26);
                }else{
                    answer+=(char)(ch+n);
                }
            }
        }

        return answer;
    }
}