import sys
file_name = sys.argv[1]
file = open(file_name, 'r')

nums = []
for i in file:
    nums.append(int(i))

nums.sort()
mean_elem = nums[len(nums)//2]
res = 0
for i in nums:
    res += abs(mean_elem - i)
    
print(res)
