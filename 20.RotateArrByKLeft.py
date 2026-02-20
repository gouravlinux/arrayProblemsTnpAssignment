# rotate array to the left by k positions
class Solution:
    def rotateLeft(self, ls, k):
        n = len(ls)
        res = [0] * n
        for i in range(n):
            res[i] = ls[(i + k) % n]
        return res


if __name__ == "__main__":
    ls = [1, 2, 3, 4]
    k = 11
    obj = Solution()
    res = obj.rotateLeft(ls, k)
    print(f"Rotated array: {res}")
