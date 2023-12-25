# https://leetcode.com/problems/jump-game-ii
nums = [2, 3, 0, 1, 4]

dp = [9999 for i in range(0, len(nums))]

dp[0] = 1

for i in range(1, len(nums)):

    for j in range(i -1, -1, -1):
        if nums[j] >= i - j and dp[j] > 0:
            dp[i] = min(dp[i], dp[j] + 1)


print(dp[len(nums) - 1] - 1)