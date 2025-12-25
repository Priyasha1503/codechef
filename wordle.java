
#https://www.codechef.com/problems/WORDLE?tab=statement

import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc =new Scanner(System.in);
		int t=sc.nextInt();
		while(t>0)
		{
	
		    String hs=sc.next();
		    String gs=sc.next();
		    String res=" ";

		    for(int i=0;i<5;i++)
		    {
		        if(hs.charAt(i)==gs.charAt(i))
		        res=res+'G';
		        else
		        res=res+'B';
		    }
		    System.out.println(res);
	        t-=1;
		    
		}
	

	}
}
