# Find missing number if array contains all elements from 1 to n except one
class Solution:
    def findMissingNum(self, ls):
        n = len(ls)
        listSum = sum(ls)
        sumOfnNums = n * (n+1)/2
        return sumOfnNums - listSum
if __name__ == '__main__':
    ls = [1, 5, 2, 4, 0]
    obj = Solution()
    res = obj.findMissingNum(ls)
    print(f"Missing Number in the array: {int(res)}")