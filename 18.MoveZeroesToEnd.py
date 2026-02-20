class Solution:
    def moveZeroesToEnd(self, ls):
        n = len(ls)
        nextNonZero = 0
        i = 0
        while i < n:
            if ls[i] != 0:
                # swap
                ls[i], ls[nextNonZero] = ls[nextNonZero], ls[i]
                i += 1
                nextNonZero += 1
            else:
                # if ls[i] is 0
                i += 1


if __name__ == "__main__":
    ls = [0, 2, 0, 3, 4, 6, 0, 8, 0]
    obj = Solution()
    obj.moveZeroesToEnd(ls)
    print(f"Updated list: {ls}")
