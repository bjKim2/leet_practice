package com.leet.base;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] strs = {"aa","ab"};
		int len = strs.length;
		
		String maxstr = strs[0], tmpstr = "";
		boolean on_off= true;;
		
		System.out.println(strs.length);
		for (int i=0; i < len ; i++) {
			System.out.println(strs[i]);
			for(int j=i+1; j < len; j++) {
				int k = 0;
				tmpstr = "";
                if(strs[i].length() >0 && strs[j].length() > 0){ 
                    
                    on_off = true;
                    while(on_off){


                        if (strs[i].charAt(k) == strs[j].charAt(k)) {
                            tmpstr += strs[i].charAt(k);

                            if(k == strs[i].length()-1  || k == strs[j].length() - 1) {
                                if (tmpstr.length() <= maxstr.length()) {
                                maxstr = tmpstr;
                            }                                
                                on_off = false;
                            }else {
                                k++;
                            }
                            
                        }else {
                            if (tmpstr.length() <= maxstr.length()) {
                                maxstr = tmpstr;
                            }
                            on_off = false;

                        }

                    }
                }else{
                    maxstr = "";
                }
			}
				
		}
		System.out.println(maxstr);
        //return maxstr;
	}

}
