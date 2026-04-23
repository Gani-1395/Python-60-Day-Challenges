def Data_process(nums):
    for num in nums:
        count=0
        for i in range (1,num+1):
            if num % i == 0:
                count+=1
        if count == 2:
            nums.remove(num)
    nums=[i*i for i in nums]
    nums.sort()
    new_nums=[]
    for i in range (len(nums)):
        new_nums.append(nums.pop())
    return new_nums
nums=[5,12,7,20,33,18,2]
print(Data_process(nums))
v]67u