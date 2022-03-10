nums = [1,100,1,2,1,3,1,4]
key = 1
count = nums.count(key)
print(count)
list = []
tmp = 0
for i in range(count):
    
    tmp = nums.index(key,tmp,len(nums)) +1
    if (tmp == len(nums)):
        break
    list.append(nums[tmp])
list.sort()
print(list)
tmp1  = -1
count = 0
max = 0
for i in list:
    if(tmp1 == i):
        count +=1
    else:
        if(max <= count):
            max = count
            result = tmp1
            
        count = 0
        tmp1 = i
        
        
    

print(nums.index(key,2,3))

# leat code 제출코드
#         count = nums.count(key)
#         list = []
#         tmp = 0
#         for i in range(count):

#             tmp = nums.index(key,tmp,len(nums)) +1
#             if (tmp == len(nums)):
#                 break
#             list.append(nums[tmp])
#         list.sort()
#         print(list)
#         tmp1  = list[0]
#         result = 0
#         count = 0
#         max = -1
#         for i in list:
#             print(tmp1,count,max)
#             if(tmp1 == i ):
                
#                 count +=1
#                 if(max < count):
#                     max = count
#                     result = tmp1
#             else:
#                 if(max < count):
#                     max = count
#                     result = tmp1

#                 count = 1
#                 tmp1 = i
        
#         return result
