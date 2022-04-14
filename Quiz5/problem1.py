import random
nums = []
for i in range(10):
  nums.append(random.randint(0,100))

print(nums)

mini = min(nums)
nums.insert(nums.index(mini), nums[0])
nums.pop(0)
nums.remove(mini)
mini2 = min(nums)
nums.insert(0, mini)
print(nums)
nums.insert(nums.index(mini2), nums[1])
nums.pop(1)
nums.remove(mini2)
nums.insert(1, mini2)
print(nums)