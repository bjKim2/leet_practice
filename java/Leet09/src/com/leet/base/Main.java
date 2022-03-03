package com.leet.base;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x =121;
		int y = x;
		boolean answer=true;
		int jari=0;
        
        // 양수일 때만 실
        if(x>0){
        	//몇 자리숫자인지 확인
            while(true) {
			if(x==0) {
				break;
			}
			x /= 10;
			jari +=1;
            }
            
            // 자리숫자만큼 배열 선언
            int[] stj = new int[jari];

            for (int i=0 ; i<jari ; i++) {
                stj[i] = y % 10;
                y/=10;

            }
            
            int j= 0;


            // 첫 자리랑 막자리수부터 비교하면서 안으로 한칸씩 들어가면서 비교 
            while(true) {	
            	// 앞에서부터 비교한 인덱스가 뒤에서 부터 비교한 인덱스보다 뒤에가면 브레이크
            	if(stj.length -1 - j <= j){
                    answer = true;
                    break;

                
            	}else if(stj[j] != stj[stj.length-1 -j]) {
                    answer=false;
                    break;
                }
                j++;
            }
	    
            
        }else if(x == 0 ){
            answer = true;
        }else{
            answer=false;
        }
		
		
		System.out.println(answer);
	}

}
