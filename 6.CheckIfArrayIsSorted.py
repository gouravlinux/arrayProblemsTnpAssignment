class Solution:
    def isSorted(self, ls):
        sorted = True
        for i in range(len(ls)-1):
            if (ls[i]>ls[i+1]):
                sorted = False
        return sorted

if __name__ == '__main__':
    ls = [6, 5, 4, 3, 9]
    obj = Solution()
    if (obj.isSorted(ls)):
        print("list is sorted")
    else:
        print("list is not sorted")
