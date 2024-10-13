nums = [32, 423, 125, 75, 8]

num = nums[0]

for i in nums:
    if i < num:
        num = i
print(num)

for i in nums:
    if i > num:
        num = i
print(num)
