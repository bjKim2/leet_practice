from multiprocessing.sharedctypes import Value


nums = [1,2,1,2,1,3,1,4,1,10]
key = 1
list = []
count = nums.count(key)
tmp = 0
for i in range(count):
    # list.append( nums.index(key,tmp,len(nums))+1)
    tmp = nums.index(key,tmp,len(nums))+1
    list.append(nums[tmp])
print(list)
l2 = dict([x,list.count(x)] for x in set(list))
print(l2)
print(max(l2, key=l2.get))

# return result