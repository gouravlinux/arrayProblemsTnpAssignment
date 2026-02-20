class Solution:
    def findLeaders(self, ls):
        # optimized -> O(n)
        res = []
        n = len(ls)
        maxEle = ls[n-1]
        for i in range(n-2, -1, -1):
            if (ls[i] > maxEle):
                maxEle = ls[i]
                res.append(ls[i])
        return res

if __name__ == '__main__':
    ls = [5, 4, 2, 3, 1]
    obj = Solution()
    res = obj.findLeaders(ls)
    print(f"Leader elements list: {res}")
