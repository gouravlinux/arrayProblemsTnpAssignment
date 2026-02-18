# Rotate the array to the right by k positions
class Solution:
    def rotateArray(self, ls, k):
        n = len(ls)
        updatedLs = [0] * n
        for i in range(n):
            updatedLs[(i + k) % n] = ls[i]
        return updatedLs
if __name__ == '__main__':
    ls = [5, 6, 4, 2, 4, 2, 3]
    k = 10
    obj = Solution()
    updatedLs = obj.rotateArray(ls, k)
    print(updatedLs)
