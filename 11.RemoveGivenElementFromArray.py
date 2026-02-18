class Solution:
    def findItem(self, item, ls):
        for i in range(len(ls)):
            if (ls[i] == item):
                return i
        return -1
    def removeFromArr(self, ls, item):
        index = self.findItem(item, ls)
        if (index == -1):
            print("Element not found")
            return -1# element not found
        else:
            for i in range(index+1,len(ls)):
                ls[i-1] = ls[i]
            ls.pop()
            return index
if __name__ == '__main__':
    ls = [1, 5 ,9, 6]
    obj = Solution()
    print(obj.removeFromArr(ls, 9))
    print(ls)