class Solution:
    def findAllSubArr(self, ls):
        n = len(ls)
        res = []
        res.append([])
        for i in range(n):
            for j in range(i, n):
                res.append(ls[i : j + 1])
        return res


if __name__ == "__main__":
    obj = Solution()
    ls = [1, 2, 3]
    res = obj.findAllSubArr(ls)
    print(f"All subArrays: {res}")
