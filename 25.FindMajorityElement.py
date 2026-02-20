class Solution:
    def findMajEl(self, ls):
        n = len(ls)
        res = int()
        freqDict = {}
        for i in ls:
            if (i in freqDict):
                freqDict[i] += 1
            else:
                freqDict[i] = 1
        for i in freqDict.keys():
            if (freqDict[i] > n/2):
                res = i
                break
        return res

if __name__ == '__main__':
    ls = [1, 2, 2, 2]
    obj = Solution()
    res = obj.findMajEl(ls)
    print(res)

