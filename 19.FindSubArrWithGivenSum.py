class Solution:
    def findSubArr(self, ls: list[int], target: int) -> int:
        freqDict = {0: 1}
        prefixSum = 0
        cnt = 0
        for i in ls:
            prefixSum += i
            findPS = prefixSum - target
            if (findPS in freqDict):
                cnt += freqDict[findPS]
            if (prefixSum in freqDict):
                freqDict[prefixSum] += 1
            else:
                freqDict[prefixSum] = 1
        return cnt
if __name__ == '__main__':
    ls = [1, 2, 3]
    target = 3
    obj = Solution()
    cnt = obj.findSubArr(ls, target)
    print("No of subArrays:", cnt)