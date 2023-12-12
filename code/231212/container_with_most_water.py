# https://leetcode.com/problems/container-with-most-water/

height = [1,2, 1]


left = 0
right = len(height) - 1
result = 0

while left < right:
    size = abs(right - left) * min(height[left], height[right])

    result = max(result, size)

    if height[left] > height[right]:
        right -= 1
    else:
        left += 1
    


print(result)