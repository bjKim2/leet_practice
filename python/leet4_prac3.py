class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m= nums1
        n = nums2
        if(len(m)<len(n)):    
            tmp = m
            m = n
            n = tmp
        
        
        
        all_ind = (len(m) +len(n)-1) //2
        n_ind = len(n) //2
        m_ind = all_ind -n_ind

        n_even = 0
        m_even = 0
        all_len = len(m) + len(n)
        all_even = 0

        if(all_len % 2 == 0):
            all_even = 1
        elif(all_len % 2 ==1):
            all_even = 0

        if(len(n) ==0 ):
            n_even = 2
        else:
            if(len(n) % 2 ==0):
                n_even = 1
            else:
                n_even = 0
        if(len(m) ==0 ):
            m_even = 2
        else:
            if(len(m) % 2 ==0):
                m_even = 1
            else:
                m_even = 0
        print("m_ind , n_ind, all_ind",m_ind , n_ind , all_ind)

        c_ind =1
        result = 0

        if(n_even != 2):
                
            if(m[m_ind] > n[n_ind] and all_even == 0):

                if(n_even == 1):
                    m_ind -=1
                elif(m_even == 1):
                    m_ind -=1

            if(all_even == 0):
                if(m[m_ind] >= n[n_ind]): 
                    c_ind = (len(n) - n_ind)//2
                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기, c
                        if(m[m_ind-c_ind] < n[n_ind - c_ind]):
                            c_ind = c_ind // 2
                        else:
                            m_ind -= c_ind
                            n_ind += c_ind
                            c_ind = c_ind //2

                        if(c_ind == 0):
                            break
                        print("c_ind",c_ind)
                    #   정답 체크 c_ind 가 1이고 

                    try:
                        if(m[m_ind] <= n[n_ind+1] and m[m_ind -1] <= n[n_ind]):
                            if(m[m_ind] >= n[n_ind]):
                                result = m[m_ind]
                            else:
                                result = n[n_ind]
                        elif(m[m_ind] <= n[n_ind+1]):
                            result = m[m_ind]
                        elif(m[m_ind -1] <= n[n_ind]):
                            result = n[n_ind]
                    except:
                        if(n_ind == len(n)-1):
                            result = m[m_ind]

                elif(m[m_ind] < n[n_ind]):
                    if(len(n) > 1):
                        c_ind = (len(n) + 1 - n_ind)//2
                    else:
                        c_ind = 0
                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기, c
                        if(m[m_ind+c_ind] > n[n_ind - c_ind]):
                            c_ind = c_ind // 2
                        else:
                            m_ind += c_ind
                            n_ind -= c_ind
                            c_ind = c_ind //2

                        if(c_ind == 0):
                            break

                        # if(m[m_ind+1] >= n[n_ind] or m[m_ind] > n[n_ind-1]):
                        #     if(m[m_ind] >= n[n_ind]):
                        #         result = n[n_ind]
                        #     else:
                        #         result = m[m_ind]
                    try:    
                        if(m[m_ind] >= n[n_ind-1]):
                            result = m[m_ind]
                    except:
                        if(n_ind==0) :
                            result = m[m_ind]
                    try:
                        if(m[m_ind +1] >= n[n_ind]):
                            result = n[n_ind]
                    except:
                        if(m_ind == len(m) -1):
                            result = m[m_ind]
            elif(all_even == 1):
                if(m[m_ind] >= n[n_ind]):
                    c_ind = (len(n) - n_ind)//2
                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기, c
                        if(m[m_ind-c_ind] < n[n_ind - c_ind]):
                            c_ind = c_ind // 2
                        else:
                            m_ind -= c_ind
                            n_ind += c_ind
                            c_ind = c_ind //2

                        if(c_ind <= 1):
                            break

                    # 정답체크
                    # 제일 큰 n이 m_ind -1에 위치한 m보다 작다면

                    try:
                        if( n_ind == len(n)-1 and m[m_ind -1] >= n[n_ind]):
                            result = (m[m_ind] + m[m_ind -1])/2
                    except:
                        print("x")
                    # n_ind +1 이 m_ind-1 보다 크다면
                        try:
                            if(n[n_ind+1] >= m[m_ind-1]):
                                result = (m[m_ind -1] +n[n_ind+1])/2
                            elif(m[m_ind] <= n[n_ind+1] and m[m_ind -1] <= n[n_ind]):
                                result = (m[m_ind] + n[n_ind]) /2
                        except:
                            if(n_ind == len(n)-1 and m_ind == 0):
                                result = (m[m_ind] + n[n_ind]) /2

                elif(m[m_ind] < n[n_ind]):
                    
                    if(len(n) > 1):
                        c_ind = (len(n) + 1 - n_ind)//2
                    else:
                        c_ind = 0

                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기, c
                        if(m[m_ind+c_ind] > n[n_ind] or m[m_ind] > n[n_ind-c_ind]):
                            c_ind = c_ind // 2
                        else:
                            m_ind += c_ind
                            n_ind -= c_ind
                            c_ind = c_ind //2

                        if(c_ind == 0):
                            break
                    print("4444m_ind , n_ind, all_ind",m_ind , n_ind , all_ind)
                    # 정답체크
                   
                    try:
                        if(m[m_ind] <= n[n_ind] and m[m_ind +1] <= n[n_ind]):
                            result = (m[m_ind] + m[m_ind +1])/2
                        elif(m[m_ind] > n[n_ind]):
                            result = (m[m_ind] + n[n_ind]) /2
                        
                    except:
                        print("zz")
                    # n_ind +1 이 m_ind-1 보다 크다면

                        try: 
                            if(n[n_ind-1] <= m[m_ind+1]):
                                result = (m[m_ind +1] +n[n_ind-1])/2
                            elif(m[m_ind] >= n[n_ind-1] and m[m_ind +1] >= n[n_ind]):
                                result = (m[m_ind] + n[n_ind]) /2
                        except:
                            if(n_ind == 0 and m_ind == len(m)-1):
                                result = (m[m_ind] +n[n_ind])/2
        else:
            if(len(m) % 2== 0 ):
                result = (m[len(m)//2] + m[(len(m)//2)  -1])/2
            else:
                result = m[len(m)//2] 
            
                
        print("all_ind : ",all_ind , "m_ind :",m_ind,"n_ind :",n_ind,"result:",result )
        return result