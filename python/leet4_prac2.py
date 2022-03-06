from inspect import classify_class_attrs
from os import scandir
# m크기의 경우의 수 0,1  0,0 1,0 1,1 2,1 1,2 

# m보다 n 이 더 길이 길도록 if문 쓰기 

# index 설정 시 0 이하로 떨어 질때는 0 으로 
m = [1,3,5,7]
n = [6,8,10,12]
m_length = len(m)
n_length = len(n)

m_index = len(m) // 2 
n_index = len(n) // 2

if (m_index !=0):
    n_preindex = n_index-1
else:
    n_preindex = n_index

if (m_index !=0):
    m_preindex = m_index-1
else:
    m_preindex = m_index

m_leftmax = m[m_preindex]
m_rightmin = m[m_index]

n_leftmax = n[n_preindex]
n_rightmin = n[n_index]

if (m[m_length-1] < n[0]):
    if ({m_length + n_length} % 2 == 0):
        result_nindex = ((m_length + n_length) / 2) - m_length
        


print(m+n)

# left min > rightmax 



