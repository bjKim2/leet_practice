package com.leet.base;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1,1,2,3};
		
		int len = nums.length;
		int count = 1;
		int index = 1;
		for(int i = 1 ; i < len ; i++) {
			if(nums[i] == nums[i-1]) {
				
				LoopOut:
				for(int j = i;j<len ;j++) {
					if(nums[i-1] != nums[j]) {
						nums[index] = nums[j];
						i = j;
						count ++;
						index ++;
						break LoopOut;
								
					}else {
						nums[j] = 999;
					}
				}
				
			}else {
				index ++;
				count +=1;
			}
		}
		System.out.println(count);
	}

}
