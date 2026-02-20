class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        n = len(nums)
        smallest = nums[0]
        maxDiff = -1
        for i in range(1, n):
            if (nums[i]>smallest):
                diff = nums[i] - smallest
                maxDiff = max(maxDiff, diff)
            else:
                smallest = nums[i]
        return maxDiff
if __name__ == '__main__':
    obj = Solution()
    ls = [7, 1, 5, 4]
    res = obj.maximumDifference(ls)
    print(res)
    