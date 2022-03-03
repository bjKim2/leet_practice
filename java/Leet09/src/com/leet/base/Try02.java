package com.leet.base;

public class Try02 {
	
	public void try02() {
		int x =12321;
		int compare1;
		int compare2=0;
		
		
		compare1 = x;
		
		
		boolean answer=true;

		while(x!=0) {
			compare2 =compare2*10 + x%10; 
		}
		
		if (compare1 == compare2) {
			answer= true;
		}else {
			answer = false;
		}
		if(compare1 <0) {
			answer =false;
		}
		System.out.println("222");
	}	
}
