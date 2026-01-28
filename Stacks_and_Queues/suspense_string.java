#https://www.codechef.com/practice/course/stacks-and-queues/STAQUEP/problems/SUSSTR


import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t=sc.nextInt();
		sc.nextLine();
		while(t-- >0)
		{
		    int n=sc.nextInt();
		    sc.nextLine();
		    String s = sc.nextLine();
		    ArrayDeque<Character> res_que = new ArrayDeque<Character>();
		    int turn=0;
		    int alice=0;
		    int bob=s.length()-1;
		    while(alice<=bob)
		    {
		        if(turn%2==0) //alice's turn -lexicographically small
		        {
		            char ch=s.charAt(alice);
		            if(ch=='0'){
		                res_que.addFirst(ch);
		            }
		            else{
		                res_que.addLast(ch);
		            }
		            alice++;
		        }
		        else{
		            char ch = s.charAt(bob);
		            if(ch=='0'){
		                res_que.addLast(ch);
		            }
		            else{
		                res_que.addFirst(ch);
		            }
		           bob--;
		        }
		        turn+=1;
		    }
		    for(char ch:res_que)
		    {
		        System.out.print(ch);
		    }
		    System.out.println();
		}


	}
}
