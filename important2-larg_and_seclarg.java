
#https://www.codechef.com/practice/course/arrays/ARRAYS/problems/LARGESECOND

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt();
            int[] a = new int[n];

            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }
            // Your code goes here
            int maxs=-1;
            int sec_maxs=-1;
            
            for(int x=0;x<n;x++)
            {
                if(a[x]>maxs){
                    sec_maxs=maxs;
                    maxs=a[x];
                    
                }
                else if (sec_maxs<a[x] && a[x]<maxs)
                sec_maxs=a[x];
            }
            System.out.println(maxs+sec_maxs);
            
        }
    }
}
