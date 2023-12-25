# https://leetcode.com/problems/jump-game/

nums = [3, 2, 1, 0, 4]
result = True
possible_nums = [False for i in range(0, len(nums))]
possible_nums[0] = True
for i in range(1, len(nums)):
    start_position = i - 1

    for j in range(start_position, -1, -1):
        if possible_nums[j] and nums[j] >= i - j:
            possible_nums[i] = True
            break

result = possible_nums[len(possible_nums) - 1]

print(result)
    