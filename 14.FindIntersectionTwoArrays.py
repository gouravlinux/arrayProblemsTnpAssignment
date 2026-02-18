class Solution:
    def findIntersection(self, ls1, ls2):
        set1 = set(ls1)
        set2 = set(ls2)
        intersectionSet = set1.intersection(set2)
        return intersectionSet

if __name__ == '__main__':
    ls1 = [1, 2, 2, 3, 4]
    ls2 = [5, 6, 2, 7, 10]
    obj = Solution()
    intersectionSet = obj.findIntersection(ls1, ls2)
    print(intersectionSet)
         