class Solution:
    def prodOfArr(self, ls):
        n = len(ls)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * ls[i - 1]
        prod = 1
        for i in range(n - 2, -1, -1):
            prod = prod * ls[i + 1]
            res[i] = res[i] * prod

        return res


if __name__ == "__main__":
    ls = [1, 2, 3, 4]
    obj = Solution()
    res = obj.prodOfArr(ls)
    print(res)
