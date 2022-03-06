
def ifswitch(m,n):

    if(len(m)<len(n)):    
        tmp = m
        m = n
        n = tmp
    return m,n

def balancing(m_ind,n_ind):
    if (m_ind > len(m)-1):
        bal = m_ind - len(m)-1
        m_ind = len(m) - 1
        n_ind += bal
    if (m_ind < 0):
        bal = 0 - m_ind
        m_ind = 0
        n_ind -= bal
    if (n_ind > len(n)-1):
        bal = n_ind -len(n)-1
        n_ind = len(n) - 1
        m_ind += bal
    if (n_ind < 0):
        bal = 0 - n_ind
        n_ind = 0
        m_ind -= bal
    return  m_ind,n_ind
m = [1,3,5,7,9]
n = [6,8,10,12,13]

# n이 더 길면 m 과 바꾼다 . m 이 더 길거나 같다.
m,n = ifswitch(m,n)
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
i = 2
while(True):
    if(m[m_ind] > n[n_ind]):
        m_ind -= all_ind//i
        n_ind += all_ind//i
        m_ind, n_ind =balancing(m_ind,n_ind)
    if(m[m_ind] < n[n_ind]):
        m_ind += all_ind//i
        n_ind -= all_ind//i 
        m_ind, n_ind =balancing(m_ind,n_ind)

    if(all_ind//i == 0):
        break
    
    i*=2    

if ((len(m) +len(n))% 2 == 0):
    if(len(m)  == len(n)):
        resuilt = (m[m_ind] +n[n_ind])/2
    else:
        if(n_ind == len(n) -1 or n_ind == 0):
            result = (m[m_ind] +m[m_ind+1])/2
        else:
            result = (m[m_ind] +n[n_ind])/2
else:
    if(m[m_ind] > n[n_ind]):
        result = m[m_ind]
    else:
        result = n[n_ind]
        
    


# 함수가 크면 바꾸는 재귀 함수로 설정






class Solution(object):
    
    c