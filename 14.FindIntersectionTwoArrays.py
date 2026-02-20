class Solution:
    def findIntersection(self, ls1, ls2):
        ls1Set = set(ls1)
        ls2Set = set(ls2)
        intersectionSet = ls1Set.intersection(ls2Set)
        return intersectionSet
if __name__ == '__main__':
    ls1 = [1, 2, 2, 3, 4]
    ls2 = [5, 6, 2, 7, 10, 3]
    obj = Solution()
    intersectionSet = obj.findIntersection(ls1, ls2)
    print(intersectionSet)
         