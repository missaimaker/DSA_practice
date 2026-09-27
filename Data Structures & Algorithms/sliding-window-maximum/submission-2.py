class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, n in enumerate(nums):
            # Remove indices outside the window
            while q and q[0] < i - k + 1:
                q.popleft()

            # Remove smaller values
            while q and nums[q[-1]] <= n:
                q.pop()

            q.append(i)

            # Start adding answers once window reaches size k
            if i >= k - 1:
                res.append(nums[q[0]])

        return res