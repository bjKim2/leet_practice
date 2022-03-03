package com.leet.base;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String s = "LVIII";
		
		//('I', 'V', 'X', 'L', 'C', 'D', 'M').
		int index =0;
		int len = s.length();
		int result =0;
		
		for(int i = 0; i<len ; i++) {
			if(len -1 - i >= 1) {
				switch(s.charAt(i)) {
				case 'M':
					result += 1000;
					break;
				case 'D':
					result += 500;
					break;
				case 'C':
					if(s.charAt(i+1) == 'D') {
						i++;
						result += 400;
					}else if(s.charAt(i+1) == 'M'){
						i++;
						result += 900;
					}else {
						result += 100;
					}
					break;
				case 'L':
					result += 50;
					break;
				case 'X':
					if(s.charAt(i+1) == 'L') {
						i++;
						result += 40;
					}else if(s.charAt(i+1) == 'C'){
						i++;
						result += 90;
					}else {
						result += 10;
					}
					break;
				case 'V':
					result += 5;
					break;
				case 'I':
					if(s.charAt(i+1) == 'V') {
						i++;
						result += 4;
					}else if(s.charAt(i+1) == 'X'){
						i++;
						result += 9;
					}else {
						result += 1;
					}
					break;
				} //switch
				
			}else {
				switch(s.charAt(i)) {
				case 'M':
					result += 1000;
					break;
				case 'D':
					result += 500;
					break;
				case 'C':

					result += 100;
					
					break;
				case 'L':
					result += 50;
					break;
				case 'X':

					result += 10;
				
					break;
				case 'V':
					result += 5;
					break;
				case 'I':
					result += 1;
					
					break;
				
				
				}
		
		
			}
		
		

		}
		System.out.println(result);

	}
}
