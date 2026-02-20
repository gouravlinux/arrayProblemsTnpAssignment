class Solution:
    def findPeak(self, ls):
        n = len(ls)
        res = self.solve(ls, 0, n - 1)
        return res

    def solve(self, ls, s, e):
        if s >= e:
            return -1
        mid = int(s + (e - s) / 2)
        if ls[mid] > ls[mid - 1] and ls[mid] > ls[mid + 1]:
            return ls[mid]
        # if mid is at left slope
        if ls[mid] > ls[mid - 1] and ls[mid] < ls[mid + 1]:
            s = mid + 1
            return self.solve(ls, s, e)
        # if mid is on right slope
        elif ls[mid] < ls[mid - 1] and ls[mid] > ls[mid + 1]:
            e = mid - 1
            return self.solve(ls, s, e)
        # if mid is at valley
        elif ls[mid] < ls[mid - 1] and ls[mid] < ls[mid + 1]:
            return self.solve(ls, s, mid - 1)
            # or return self.solve(ls, mid+1, e)


if __name__ == "__main__":
    ls = [1, 2, 1, 3, 1, 2, 1, 2, 1]
    obj = Solution()
    res = obj.findPeak(ls)
    print(res)
