class Solution:
    def sortArr(self, ls):
        n = len(ls)
        nextZero = 0
        nextTwo = n - 1
        i = 0 
        while i <= nextTwo:
            if ls[i] == 0:
                ls[i], ls[nextZero] = ls[nextZero], ls[i]
                nextZero += 1
                i += 1

            elif ls[i] == 2:
                ls[i], ls[nextTwo] = ls[nextTwo], ls[i]
                nextTwo -= 1

            else:
                i += 1


if __name__ == "__main__":
    obj = Solution()
    ls = [2, 0, 1, 2, 0, 0, 1]
    obj.sortArr(ls)
    print(ls)
