class Solution:
    def countFreq(self, ls):
        freqDict = {}
        for i in ls:
            if i not in freqDict:
                freqDict[i] = 1
            else:
                freqDict[i] += 1
        return freqDict

if __name__ == '__main__':
    ls = [4, 5, 6, 7, 7, 6, 5]
    obj = Solution()
    print(f"Freq Dictionary: {obj.countFreq(ls)}")