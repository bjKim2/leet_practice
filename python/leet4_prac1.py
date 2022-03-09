


m = [1,3,5,7,9]
n = [6,8,10,12,13]

# n이 더 길면 m 과 바꾼다 . m 이 더 길거나 같다.\
def ifswitch(m,n):
    if(len(m)<len(n)):    
        tmp = m
        m = n
        n = tmp
    return m,n

##이제 길이가 m >= n 이다. 
# 배열 두개를 합치지않고  중앙값을 구하려면
# m,n 의 중간 값 을 비교 작은 배열이 우측이동 큰쪽이 좌측이동 
# 이동 값이 같아야되는데 이동값은 남은 배열의 절반
# 이동 값이 반나누다보면 1이 남게 되는 경우 1칸 이동

# 전체 개수가 짝수 일 떄 2개 값을 찾아 나눔
# 전체 개수가 홀수일 떄

all_ind = (len(m) +len(n))-1//2
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

if(m[m_ind] > n[n_ind] and all_even == 1):
    if(all_len % 2 == 1):
        if(n_even == 1):
            m_ind -=1
        elif(m_even == 1):
            m_ind -=1

c_ind =1
result = 0

while(True):
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
                
            #   정답 체크 c_ind 가 1이고 
            
                    
            if(m[m_ind] <= n[n_ind+1] and m[m_ind -1] <= n[n_ind]):
                if(m[m_ind] >= n[n_ind]):
                    result = m[m_ind]
                else:
                    result = n[n_ind]
            elif(m[m_ind] <= n[n_ind+1]):
                result = m[m_ind]
            elif(m[m_ind -1] <= n[n_ind]):
                result = n[n_ind]
                
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
                
            if(m[m_ind] <= n[n_ind+1] and m[m_ind -1] <= n[n_ind]):
                if(m[m_ind] >= n[n_ind]):
                    result = n[n_ind]
                else:
                    result = m[m_ind]
            elif(m[m_ind] <= n[n_ind+1]):
                result = m[m_ind]
            elif(m[m_ind -1] <= n[n_ind]):
                result = n[n_ind]

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
            if( n_ind == len(n)-1 and m[m_ind -1] >= n[n_ind]):
                result = (m[m_ind] + m[m_ind -1])/2
            
            # n_ind +1 이 m_ind-1 보다 크다면
            if(n[n_ind+1] >= m[m_ind-1]):
                result = (m[m_ind -1] +n[n_ind+1])/2
            elif(m[m_ind] <= n[n_ind+1] and m[m_ind -1] <= n[n_ind]):
                result = (m[m_ind] + n[n_ind]) /2
            
        elif(m[m_ind] < n[n_ind]):
            if(len(n) > 1):
                c_ind = (len(n) + 1 - n_ind)//2
            else:
                c_ind = 0
                
            while(True): # c_ind 로 n>m 일 때 바꾸지 않기, c
                if(m[m_ind-c_ind] > n[n_ind - c_ind]):
                    c_ind = c_ind // 2
                else:
                    m_ind -= c_ind
                    n_ind += c_ind
                    c_ind = c_ind //2
                    
                if(c_ind <= 1):
                    break
            
            # 정답체크
    
            if( n_ind == 0 and m[m_ind +1] <= n[n_ind]):
                result = (m[m_ind] + m[m_ind +1])/2
            
            # n_ind +1 이 m_ind-1 보다 크다면
            if(n[n_ind-1] <= m[m_ind+1]):
                result = (m[m_ind +1] +n[n_ind-1])/2
            elif(m[m_ind] >= n[n_ind-1] and m[m_ind +1] >= n[n_ind]):
                result = (m[m_ind] + n[n_ind]) /2
                
            
        
        
        
        
        
        
        
        
        
        
        
        
#     if(m[m_ind] < n[n_ind]):


#     if(all_ind//i == 0):
#         break
    
#     i*=2    

# if ((len(m) +len(n))% 2 == 0):
#     if(len(m)  == len(n)):
#         result = (m[m_ind] +n[n_ind])/2
#     else:
#         if(n_ind == len(n) -1 or n_ind == 0):
#             result = (m[m_ind] +m[m_ind+1])/2
#         else:
#             result = (m[m_ind] +n[n_ind])/2
# else:
#     if(m[m_ind] > n[n_ind]):
#         result = m[m_ind]
#     else:
#         result = n[n_ind]
        
    


# 함수가 크면 바꾸는 재귀 함수로 설정



