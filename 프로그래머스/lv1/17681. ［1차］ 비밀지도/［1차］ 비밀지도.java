class Solution {
        public String toBinaryString(int n){
        StringBuilder sb=new StringBuilder("");
        while (n > 0) {
            sb.append(Integer.toString(n%2));
            n/=2;
        }

        return sb.reverse().toString();
    }
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = {};
        String[] maps=new String[arr1.length];
        Solution pg_17681=new Solution();
        for(int i=0; i<arr1.length; i++){
            maps[i]=pg_17681.toBinaryString(arr1[i]|arr2[i]);
            System.out.println(maps[i]);
            maps[i]=maps[i].replace("1", "#");
            maps[i]=maps[i].replace("0", " ");

            while (maps[i].length()<n){
                maps[i]=' '+maps[i];
            }
        }

        return maps;
    }
}