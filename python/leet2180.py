#num = 134
l1 = []

sum = (int(num) //20 ) * 10
print(sum)
last = (int(num) %20) 
num /= 10
l1 = []
while(int(num) !=0):

    l1.append(int(num % 10))
    num /= 10
eve = 0
for i in l1:
    eve += i

if(last>=10):
    eve -=1
print(eve, sum)
if((eve +1)% 2 == 0):
    if(sum >0):
        sum -=1
    if(last //10 == 1):
        sum = sum + 6 + ((last-10)//2) 
    elif(last // 10 == 0):
        sum += (last+1)//2

elif((eve+1)% 2 == 1):
    if(last //10 == 1):
        sum = sum + 4 + (((last-10)+1)//2) 
    elif(last // 10 == 0):
        sum += last//2
#print(sum)

#return sum