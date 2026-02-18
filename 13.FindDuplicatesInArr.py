class Solution:
    def findDuplicates(self, ls):
        freqDict = {}
        duplicateSet = set()
        for i in ls:
            if i not in freqDict:
                freqDict[i] = 1
            else:
                freqDict[i] += 1
        for i in freqDict.keys():
            if freqDict[i] >= 2:
                duplicateSet.add(i)
        return duplicateSet


if __name__ == "__main__":
    ls = [4, 5, 4, 3, 2, 2, 1, 5, 6]
    obj = Solution()
    resSet = obj.findDuplicates(ls)
    print(resSet)