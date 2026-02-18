class Solution:
    def mergeArrays(self, ls1, ls2):
        i = 0
        j = 0
        m = len(ls1)
        n = len(ls2)
        ls3 = [0] * (m + n)
        k = 0
        while i < m and j < n:
            if ls1[i] > ls2[j]:
                ls3[k] = ls2[j]
                j += 1
                k += 1
            else:
                ls3[k] = ls1[i]
                i += 1
                k += 1
        while i < m:
            ls3[k] = ls1[i]
            i += 1
            k += 1
        while j < n:
            ls3[k] = ls2[j]
            j += 1
            k += 1
        return ls3


if __name__ == "__main__":
    ls1 = [4, 5, 6]
    ls2 = [7, 9, 11, 15]
    obj = Solution()
    ls3 = obj.mergeArrays(ls1, ls2)
    print(ls3)
