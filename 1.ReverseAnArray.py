class Solution:
    def swap(ls, i, j):
        temp = ls[i]
        ls[i] = ls[j]
        ls[j] = temp

    def reverseArray(self, ls):
        n = len(ls)
        # ls.reverse()
        # print(ls)
        i = 0
        j = n - 1
        while i < j:
            Solution.swap(ls, i, j)
            i += 1
            j -= 1


if __name__ == "__main__":
    obj = Solution()
    ls = [5, 2, 6, 8, 9]
    print(f"List before sorting: {ls}")
    obj.reverseArray(ls)
    print(f"List after sorting: {ls}")
