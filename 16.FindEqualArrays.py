class Solution:
    def findEqualArr(self, ls1, ls2):
        ls1Set = set(ls1)
        ls2Set = set(ls2)
        if (ls1Set == ls2Set):
            return True
        else:
            return False

if __name__ == '__main__':
    ls1 = [5,4,3,2,1]
    ls2 = [4,2,5,1,5]
    obj = Solution()
    isEqual = obj.findEqualArr(ls1, ls2)
    if (isEqual):
        print("The arrays are equal")
    else:
        print("The arrays are not equal")
       
    