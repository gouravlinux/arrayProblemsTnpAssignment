class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        largest = 0
        secondLargest = 0
        for i in nums:
            if largest < i:
                secondLargest = largest
                largest = i
            else:
                secondLargest = max(secondLargest, i)
        return (largest) * (secondLargest)


if __name__ == "__main__":
    obj = Solution()
    ls = [1, 5, 4, 5]
    res = obj.maxProduct(ls)
    print(res)
