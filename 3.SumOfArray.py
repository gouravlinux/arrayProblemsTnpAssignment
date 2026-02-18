class Solution:
    def sumOfArray(self, ls):
        sum = 0
        for i in ls:
            sum += i
        return sum
if __name__ == '__main__':
    ls = [5, 6, 8, 1, 11]
    obj = Solution()
    sumArr = obj.sumOfArray(ls)
    print(f"Sum of Array: {sumArr}")