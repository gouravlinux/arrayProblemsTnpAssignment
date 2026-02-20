class Solution:
    def findUnion(self, ls1, ls2):
        ls1Set = set(ls1)
        ls2Set = set(ls2)
        unionSet = ls1Set.union(ls2Set)
        return unionSet

if __name__ == '__main__':
    ls1 = [1, 2, 3, 2]
    ls2 = [4, 5, 2, 1]
    obj = Solution()
    unionSet = obj.findUnion(ls1, ls2)
    print(unionSet)