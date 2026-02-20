class Solution:
    def rearrangeArr(self, ls):
        n = len(ls)
        # mid = int(n / 2)
        ls.sort()
        res = [0] * n
        j = n - 1
        k = 0
        for i in range(0, n, 2):
            res[i] = ls[j]
            j -= 1
        for i in range(1, n, 2):
            res[i] = ls[k]
            k += 1
        return res


if __name__ == "__main__":
    ls = [5, 4, 2, 1]
    obj = Solution()
    res = obj.rearrangeArr(ls)
    print(res)
