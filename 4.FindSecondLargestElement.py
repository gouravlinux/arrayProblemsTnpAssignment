class Solution:
    def secondLargest(self, ls):
        n = len(ls)
        largest = ls[0]
        secondLarge = ls[0]
        for i in ls:
            if (i > largest):
                secondLarge = largest
                largest = i
        return secondLarge
if __name__ == '__main__':
    ls = [1, 5, 4, 6, 2]
    obj = Solution()
    res = obj.secondLargest(ls)
    print(f"Second Largest Element: {res}")
