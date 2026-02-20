class Solution:
    def findEqIdx(self, ls):
        n = len(ls)
        listSum = sum(ls)
        leftSum = 0
        rightSum = listSum
        rightSum -= ls[0]
        if leftSum == rightSum:
            return 0
        for i in range(1, n):
            leftSum += ls[i - 1]
            rightSum -= ls[i]
            if leftSum == rightSum:
                return i
        return -1


if __name__ == "__main__":
    ls = [1, 7, 3, 6, 5, 6]
    obj = Solution()
    res = obj.findEqIdx(ls)
    if res != -1:
        print("Index: ", res)
    else:
        print("No equilibrium Index")
