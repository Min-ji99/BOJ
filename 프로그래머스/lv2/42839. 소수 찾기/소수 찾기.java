import java.util.HashSet;
class Solution {
    public boolean isPrime(int n){
        if(n<2) return false;
        for(int i=2; i*i<=n; i++){
            if(n%i==0) return false;
        }
        return true;

    }

    public void permutation(String numbers, HashSet<Integer> output, boolean[] visited, int depth, StringBuilder stringBuilder){
        for(int i=0; i<visited.length; i++){
            if(visited[i]) continue;
            visited[i]=true;
            stringBuilder.append(numbers.charAt(i));
            output.add(Integer.parseInt(stringBuilder.toString()));
            permutation(numbers, output, visited, depth+1, stringBuilder);
            stringBuilder.deleteCharAt(stringBuilder.length()-1);
            visited[i]=false;
        }
    }

    public int solution(String numbers) {
        Solution makePrime=new Solution();
        int answer = 0;
        HashSet<Integer> numSet=new HashSet<>();
        makePrime.permutation(numbers, numSet, new boolean[numbers.length()], 0, new StringBuilder());

        for(Integer num : numSet){
            if(makePrime.isPrime(num)) {
                answer+=1;
                System.out.println(num);
            }
        }

        return answer;
    }
}