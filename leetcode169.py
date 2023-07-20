nums = [3, 2, 3]

d = {}
for i in range(len(nums)):
    if nums[i] not in d.keys():
        d[nums[i]] = 1
    else:
        d[nums[i]] = d[nums[i]] + 1

# print(d)

max = 0
max_key = 0

for i in d.keys():
    if d[i] > max:
        max = d[i]
        max_key = i

print(max_key)
