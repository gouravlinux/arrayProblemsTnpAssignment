class Solution:
    def findMax(self, ls):
        maxElement = ls[0] 
        for i in ls:
            maxElement = max(i, maxElement)
        return maxElement
    def findMin(self, ls):
        minElement = ls[0]
        for i in ls:
            minElement = min(i, minElement)
        return minElement
if __name__ == '__main__':
    obj = Solution()
    ls = [6, 9, 8, 6, 4]
    maxElement = obj.findMax(ls)
    minElement = obj.findMin(ls)
    print(f"Largest element: {maxElement}")
    print(f"Smallest element: {minElement}")
