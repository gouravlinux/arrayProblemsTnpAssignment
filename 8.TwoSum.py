# find pairs of elements having their sum equal to target sum
class Solution:
    def twoSum(self, ls, target):
        res = []
        n = len(ls)
        freqDict = {}
        # create hash map
        for i in ls:
            if i not in freqDict:
                freqDict[i] = 1
            else:
                freqDict[i] += 1
        for i in ls:
            if (target-i != i):
                if (target-i in freqDict):
                    if ((i,target-i) not in res and (target-i, i) not in res):
                        res.append((i, target-i))
            else:
                if (freqDict[i] >= 2):
                    if ((i, i) not in res):
                        res.append((i,i)) 
        return res

if __name__ == '__main__':
    ls = [4, 5, 6, 2, 3, 1]
    obj = Solution()
    res = obj.twoSum(ls, 6)
    print(res)
