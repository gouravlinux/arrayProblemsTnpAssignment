# Find Max. Sum of any SubArray
class Solution:
    def findMaxSumSubArr(self, ls):
        n = len(ls)
        maxSum = ls[0]
        currSum = ls[0]
        for i in range(1, n):
            currSum = max(ls[i], ls[i] + currSum)
            maxSum = max(maxSum, currSum)
        return maxSum


if __name__ == "__main__":
    obj = Solution()
    ls = [5, -6, 3, 7, -4]
    maxSum = obj.findMaxSumSubArr(ls)
    print(f"Maxium sum of subarrays: {maxSum}")
