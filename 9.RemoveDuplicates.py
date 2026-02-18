class Solution:
    def removeDuplicates(self, ls):
        st = set()
        res = []
        for i in ls:
            if i not in st:
                st.add(i)
                res.append(i)
        return res
if __name__ == '__main__':
    ls = [4, 5, 6, 7, 6, 5,3, 4, 2]
    obj = Solution()
    res = obj.removeDuplicates(ls)
    print(res)