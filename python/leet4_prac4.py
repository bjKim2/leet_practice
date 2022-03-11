

from calendar import c


m= [1,2,3]
n= [1,2,3,4]


# def ifswitch(m,n):
#     if(len(m)<len(n)):
#         tmp = m
#         m = n
#         n = tmp
#     return m,n

m, n =ifswitch(m,n)

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

print("m_ind , n_ind, all_ind",m_ind , n_ind , all_ind)

c_ind =1
result = 0
tmp_ind = 0

if(all_len % 2 ==0):
    c_ind = 1
    if(n[n_ind] == m[m_ind] ):
        return ( n[n_ind]+m[m_ind] )/2
    if(n[n_ind] < m[m_ind]):
        c_ind = (len(n) - n_ind)//2
        tmp_ind = n_ind + c_ind 
        if(tmp >=):
            while(True): # c_ind 로 n>m 일 때 바꾸지 않기, c
                if(m[m_ind-c_ind] < n[n_ind + c_ind]):
                    c_ind = (len(n)-1 - tmp_ind) //2
                    tmp_ind = n_ind + c_ind
                elif(n[n_ind] == m[m_ind] ):
                    return ( n[n_ind]+m[m_ind] )/2
                else:
                    m_ind -= c_ind
                    n_ind += c_ind
                    c_ind = c_ind //2
                    
                if((tmp_ind == len(n)-2 ):
                    break
                print("c_ind",c_ind)
        if(m[m_ind-1] >= n[n_ind]):
            
    

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

