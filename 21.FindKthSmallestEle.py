from queue import PriorityQueue


class Solution:
    def findKthSmallest(self, ls, k):#O(nlogk) approach of a min-Heap
        pq = PriorityQueue()  # min-Heap
        n = len(ls)
        for i in range(k):
            pq.put(-1 * ls[i])
        for i in range(k, n):
            item = -1 * pq.get()
            if item <= ls[i]:
                pq.put(-1 * item)
            else:
                pq.put(-1 * ls[i])
        smallestEle = -1 * pq.get()
        return smallestEle


if __name__ == "__main__":
    obj = Solution()
    ls = [1, 2, 5, 4, 3]
    k = 3
    smallestEle = obj.findKthSmallest(ls, k)
    print(f"kth Smallest element: {smallestEle}")
