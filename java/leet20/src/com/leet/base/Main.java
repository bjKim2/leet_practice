package com.leet.base;

import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		String s = "{[]}";
//		Stack<Character> arr = new Stack<Character>();
//		char[] chrs =  s.toCharArray();
//		
//		for(char c : s.toCharArray()) {
//			System.out.println(c);
//		}
//		arr.push('1');
//		arr.push('2');
//		arr.push('3');
//		for(char c : arr) {
//			System.out.println(c);
//		}
//		System.out.println(arr.pop());
//		System.out.println(arr.pop());
//		System.out.println(arr.pop());
		
		String s = "()[]{}";
		String tmp = "";
		int dir = 0;
		int count = 0;
		boolean answer = true;
		if(s.charAt(0) == ')' || s.charAt(0) == '}' || s.charAt(0) == ']' ) {
			answer = false;
		}
		
		for (int i = 0 ; i < s.length() ; i++) {
			//System.out.println(count);
			switch(s.charAt(i)){
			case '[':
				tmp += '[';
				count += 1;
				
				break;
			case '{':
				tmp += '{';
				count += 1;
				break;
			case '(':
				tmp += '(';
				count += 1;
				break;
			case ']':
				//System.out.println("tmp " + tmp + "count" +count);
				if(tmp.charAt(count-1) != '[' ) {
					answer = false;
					//return false;
				}else {
					tmp = tmp.substring(0,tmp.length()-1);
					count -= 1;
				}
				break;
			case '}':
				if(tmp.charAt(count-1) != '{' ) {
					answer = false;
					//return false;
				}else {
					tmp = tmp.substring(0,tmp.length()-1);
					count -= 1;
				}
				break;
			case ')':
				if(tmp.charAt(count-1) != '(' ) {
					answer = false;
					//return false;
				}else {
					tmp = tmp.substring(0,tmp.length()-1);
					count -= 1;
				}
				break;
			default:
				//return false;
				break;
				
				
				
				
			}//switch
			
			
		}//for
		System.out.println(answer);
		//return answer;
	}

}
