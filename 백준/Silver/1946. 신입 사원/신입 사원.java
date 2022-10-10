import java.util.*;

class Grade implements Comparable<Grade>{
    int a;
    int b;
    public Grade(int a, int b){
        this.a=a;
        this.b=b;
    }
    @Override
    public int compareTo(Grade o){
        if(o.a<this.a){
            return 1;
        }
        return -1;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
        for(int tc=0; tc<T; tc++){
            int N=sc.nextInt();
            ArrayList<Grade> scores=new ArrayList<>();
            for(int i=0; i<N; i++) {
                int a=sc.nextInt();
                int b=sc.nextInt();
                scores.add(new Grade(a, b));
            }
            Collections.sort(scores);
            int interview_score=scores.get(0).b;
            int ans=1;
            for(int j=1; j<N; j++){
                if(scores.get(j).b<interview_score){
                    ans+=1;
                    interview_score=scores.get(j).b;
                }
            }
            System.out.println(ans);
        }
        sc.close();
    }
}
