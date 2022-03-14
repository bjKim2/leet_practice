


# def ifswitch(m,n):
#     if(len(m)<len(n)):
#         tmp = m
#         m = n
#         n = tmp
#     return m,n



## 입력데이터 필터 
# 1.len(n) = 0 일 경우 리턴 clear

# if(len(n) == 0):
#     if(len(m) % 2 == 0):
#         return (m[len(m)//2] + m[(len(m)-1)//2])/2
#     else:
#         return (m[len(m)//2])

m = nums1
n = nums2

if(len(m)<len(n)):    
    tmp = m
    m = n
    n = tmp



        # def ifswitch(m,n):
        #     if(len(m)<len(n)):
        #         tmp = m
        #         m = n
        #         n = tmp
        #     return m,n

        

        ## 입력데이터 필터 
        # 1.len(n) = 0 일 경우 리턴 clear

        # if(len(n) == 0):
        #     if(len(m) % 2 == 0):
        #         return (m[len(m)//2] + m[(len(m)-1)//2])/2
        #     else:
        #         return (m[len(m)//2])

        m = nums1
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
        #이까지 그냥  정의 
        print("m_ind , n_ind, all_ind",m_ind , n_ind , all_ind)

        c_ind =1
        result = 0
        tmp_ind = 0
        
        if(len(n) == 0):
            if(len(m) % 2 ==0):
                return (m[len(m)//2]+m[(len(m)-1)//2])/2
            elif(len(m) % 2 == 1 ):
                return m[(len(m)-1)//2]

        # 전체 배열이 짝수개 일떄
        if(all_len % 2 ==0): 
            c_ind = 1
            if(n[n_ind] == m[m_ind] ):# n,m값이 같을 떄 그냥 반환
                return ( n[n_ind]+m[m_ind] )/2

            elif(n[n_ind] < m[m_ind]):# n<m 일때
                
                
                c_ind = (len(n) - n_ind)//2
                tmp_ind = n_ind 
                if(len(n)-1 - n_ind >= 1): # n 과 n max가 1단계 이상 차이날 떄 연산
                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기,
                        print("m_ind , n_ind,c_ind,tmp_ind",m_ind , n_ind , c_ind,tmp_ind)
                        if(m[m_ind-c_ind] < n[n_ind + c_ind]):
                            tmp_ind = tmp_ind + c_ind
                            c_ind = (len(n) - tmp_ind) //2
                            
                        elif(n[n_ind] == m[m_ind] ):
                            return ( n[n_ind]+m[m_ind] )/2
                        else:
                            m_ind -= c_ind
                            n_ind += c_ind
                            
                            tmp_ind = tmp_ind + c_ind
                            c_ind = (len(n) - tmp_ind) //2
                            
                        if(tmp_ind == len(n)-1 ):
                            break
                        print("case1",c_ind)


                # 정답 구분
                #n인덱스가 끝에있어서 조절이 안될 떄
                if(n_ind == len(n) -1 and len(m) == len(n)):
                    return ( n[n_ind]+m[m_ind] )/2
                elif(n_ind == len(n)-1 and m[m_ind-1] > n[n_ind]):
                    return (m[m_ind] +m[m_ind-1])/2
                elif(n_ind == len(n)-1 and m[m_ind] >= n[n_ind]):
                    return ( n[n_ind]+m[m_ind] )/2


                #1. n m n m 2.  n m m n  3.  m n n m
                if(n[n_ind+1] <= m[m_ind] and m[m_ind-1] >= n[n_ind]):
                    return (n[n_ind+1] +m[m_ind-1])/2
                elif(m[m_ind-1] >= n[n_ind]):
                    return (m[m_ind] +m[m_ind-1])/2
                elif(m[m_ind] >= n[n_ind+1]):
                    return (n[n_ind] +n[n_ind+1])/2
                else:
                    return ( n[n_ind]+m[m_ind] )/2
                # 남은 경우의 수가  n m , n m n m ,  n n m n n m m m , n n n m m n m m   

            elif(n[n_ind] > m[m_ind]):    
                
                c_ind = (n_ind+1)//2
                tmp_ind = n_ind
                
                if(n_ind >= 1): # n 과 n max가 2단계 이상 차이날 떄 연산
                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기,
                        print(m_ind,n_ind,c_ind,tmp_ind)
                        if(m[m_ind+c_ind] > n[n_ind - c_ind]):
                            tmp_ind = tmp_ind - c_ind
                            c_ind = (tmp_ind+1) //2
                            
                        elif(n[n_ind] == m[m_ind] ):
                            return ( n[n_ind]+m[m_ind] )/2
                        else:
                            
                            m_ind += c_ind
                            n_ind -= c_ind
                            tmp_ind = tmp_ind - c_ind
                            c_ind = (tmp_ind+1) //2
                            
                        if(tmp_ind == 0):
                            break
                        print("case2",c_ind)


                print(m_ind,n_ind,c_ind,tmp_ind)

                 # 정답 구분
                #n인덱스가 끝에있어서 조절이 안될 떄
                if(n_ind == 0 and len(m) == len(n)):
                    return (n[n_ind]+m[m_ind])/2
                elif(n_ind == 0 and m[m_ind+1] < n[n_ind]):
                    return (m[m_ind]+m[m_ind+1])/2
                elif(n_ind == 0 and m[m_ind] <= n[n_ind]):
                    return ( n[n_ind]+m[m_ind] )/2

            

                #1. m n m n  2.  n m m n  3.  m n n m
                if(n[n_ind-1] >= m[m_ind] and m[m_ind+1] <= n[n_ind]):
                    return (n[n_ind-1] +m[m_ind+1])/2
                elif(m[m_ind+1] <= n[n_ind]):
                    return (m[m_ind] +m[m_ind+1])/2
                elif(m[m_ind] <= n[n_ind-1]):
                    return (n[n_ind] +n[n_ind-1])/2
                else:
                    return ( n[n_ind]+m[m_ind] )/2
                # 남은 경우의 수가  n m , n m n m ,  n n m n n m m m , n n n m m n m m   


        if(all_len % 2 ==1):
            if(len(n) == 1 and len(m) ==2 ):
                if(n[0] >= m[1]):
                    return m[1]
                elif(n[0] >= m[0]):
                    return n[0]
                else:
                    return m[0]

            c_ind = 1
            if(n[n_ind] == m[m_ind] ):# n,m값이 같을 떄 그냥 반환
                return ( n[n_ind]+m[m_ind] )/2

            elif(n[n_ind] < m[m_ind]):# n<m 일때
                c_ind = (len(n) - n_ind)//2
                tmp_ind = n_ind 
                if(len(n)-1 - n_ind >= 1): # n 과 n max가 1단계 이상 차이날 떄 연산
                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기,
                        if(m[m_ind-c_ind] < n[n_ind + c_ind]):
                            tmp_ind = tmp_ind + c_ind
                            c_ind = (len(n) - tmp_ind) //2
                            
                        elif(n[n_ind] == m[m_ind] ):
                            return ( n[n_ind]+m[m_ind] )/2
                        else:
                            m_ind -= c_ind
                            n_ind += c_ind
                            tmp_ind = tmp_ind + c_ind
                            c_ind = (len(n) - tmp_ind) //2

                        if(tmp_ind == len(n)-1 ):
                            break
                        print("case3",c_ind)


                # 정답 구분
                #n인덱스가 끝에있어서 조절이 안될 떄
                
                if(n_ind == len(n)-1 and m[m_ind-1] > n[n_ind]):
                    return m[m_ind-1]
                elif(n_ind == len(n) -1 and m[m_ind]>=n[n_ind] ):
                    return n[n_ind]
                elif(n_ind == len(n) -1 and m[m_ind]<=n[n_ind] ):
                    return m[m_ind]
                #1. n m n m 2.  n m m n  3.  m n n m
                if(n[n_ind+1] <= m[m_ind] and m[m_ind-1] >= n[n_ind]):
                    return m[m_ind-1]
                elif(m[m_ind-1] >= n[n_ind] ):
                    return m[m_ind-1]
                elif(m[m_ind] >= n[n_ind+1]):
                    return n[n_ind]
                else:
                    if(m[m_ind] >= n[n_ind]):
                        return n[n_ind]
                    else:
                        return m[m_ind]
                # 남은 경우의 수가  n m , n m n m ,  n n m n n m m m , n n n m m n m m   

            elif(n[n_ind] > m[m_ind]):    
                c_ind = (n_ind+1)//2
                tmp_ind = n_ind 
                if(n_ind >= 1): # n 과 n max가 2단계 이상 차이날 떄 연산
                    while(True): # c_ind 로 n>m 일 때 바꾸지 않기,
                        print(m_ind,n_ind,c_ind,tmp_ind)
                        if(m[m_ind+c_ind] > n[n_ind - c_ind]):
                            tmp_ind = tmp_ind - c_ind
                            c_ind = (tmp_ind+1) //2
                            
                        elif(n[n_ind] == m[m_ind] ):
                            return ( n[n_ind]+m[m_ind] )/2
                        else:
                            m_ind += c_ind
                            n_ind -= c_ind
                            tmp_ind = tmp_ind - c_ind
                            c_ind = (tmp_ind+1) //2
                        if(tmp_ind == 0):
                            break
                        print("case4",c_ind)
                        


                 # 정답 구분
                #n인덱스가 끝에있어서 조절이 안될 떄
                print(m_ind,n_ind,c_ind,tmp_ind)
                if(n_ind == 0 and m_ind == len(m)-1):
                    return m[m_ind]
                elif(n_ind == 0 and m[m_ind+1] < n[n_ind]):
                    return m[m_ind]
                elif(n_ind == 0 and m[m_ind]>=n[n_ind] ):
                    return n[n_ind]
                elif(n_ind == 0 and m[m_ind]<=n[n_ind] ):
                    return m[m_ind]

                #1. m n m n  2.  n m m n  3.  m n n m
                if(n[n_ind-1] >= m[m_ind] and m[m_ind+1] <= n[n_ind]):
                    return n[n_ind-1]
                elif(m[m_ind+1] <= n[n_ind]):
                    return m[m_ind]
                elif(m[m_ind] <= n[n_ind-1]):
                    return n[n_ind-1]
                else:
                    if(m[m_ind] >= n[n_ind]):
                        return n[n_ind]
                    else:
                        return m[m_ind]
# # 메인 알고리즘
# m과 n의 인덱스 합이 중앙인덱스가 되게 함. 
# m값과 n값이 중앙값에서 같으 거리에 있게 됨
# 이동값은 남은 n인덱스의 절반
# 이동하다가 처음 m값이 n보다 작아지거나 그 반대인 경우 이동값을 반으로 계속 줄이고 이동값이 1 이되었을 때도 반전이 일어나면 그게 답
# 짝수일 경우 마지막에 반전값이 되어도 안되어도 답일 경우가 생긴다.
# 짝수일 떄는 반전이 될 경루를 막는 것을 풀어야하는가 아니면 c_ind 가 한개 남았을 떄를 따로 빼는 게 낫겠다.
 


# 메인 알고리즘의 예외
# 1. n의 끝이 중앙값을 이하인 경우
# 2. all_len 이 짝수일 떄 크로스 되는게 둘다 정답인 경우

# 홀수 일 때
# n이 작고 1예외 상황이면(중 중후라서 n이 정답이어야하기에) m인뎃스를 1줄이면 n[max] 값일떄 m이 답이 된다.
# 홀수이면 len(m)이 2이상이기 때문에 m-1이 -1이 되는 불상사가 존재하지않는다.
# 

# 짝수일 떄 
# n이 작고 중앙값이하인 -> m 2개가 답인 경우 
# 그러나 답을 알수가 없기 떄문에 조건문에 답에 대한 조건을 달순없다.
# 따라서 n이 맥스일 떄 m값과 사이에 m-1값이 존재할 경우 m 과 m-1이 답이다.
# 이 조건문 처리에서 m-1 인덱스가 존재하지 않으면 안되는데 

# n이 정답을 크로스 하고 m 2개가 답인 경우

