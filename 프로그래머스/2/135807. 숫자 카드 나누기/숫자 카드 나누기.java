import java.util.*;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        
        //각 배열의 최대 공약수 구하기
        //최대 공약수의 약수들 중 상대방 배열에 없는 가장 큰 약수 구하기
        int gcdA = arrayA[0];
        int gcdB = arrayB[0];
        
        for(int i=1; i<arrayA.length; i++) {
            gcdA = gcd(gcdA, arrayA[i]);
            gcdB = gcd(gcdB, arrayB[i]);
        }
        
        
        if(notDivide(arrayB, gcdA)) {
            answer = gcdA;
        }
           
        if(notDivide(arrayA, gcdB)) {
            if(answer < gcdB) {
                answer = gcdB;
            }
        }
        
        return answer;
    }
    
    boolean notDivide(int[] arr, int n) {
        for(int i=0; i<arr.length; i++){
            if(arr[i]%n==0) return false;
        }
        return true;
    }
    
    int gcd(int a, int b){
        if(a%b==0) return b;
        return gcd(b, a%b);
    }
    
}