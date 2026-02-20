class Solution:
    def findFirstMissingPositive(self, ls):
        ls.sort()
        n = len(ls)
        for i in range(n):
            if (ls[i] > 0):
                if (ls[i-1] <= 0):
                    return ls[i] + 1
        return 1

if __name__ == '__main__':
    ls = [-4, 6, 7, -2, 1]
    obj = Solution()
    print(obj.findFirstMissingPositive(ls))