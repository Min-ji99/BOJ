import java.util.Scanner;
/*
기능목록
1. 일의 자리가 3, 6, 9일 때 count하는 기능
2. 두자리수 이상일 때 박수 count하는 기능
 */
public class Main {
    public static void main(String[] args) {
        int answer = 0;
        Scanner sc=new Scanner(System.in);
        int number=sc.nextInt();
        for(int i=1; i<=number; i++) {
            int num=i;
            while(num>0) {
                if (num % 10 == 3 || num % 10 == 6 || num % 10 == 9) {
                    answer += 1;
                }
                num/=10;
            }
        }
        System.out.println(answer);
    }
}
