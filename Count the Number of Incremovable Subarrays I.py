class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_strictly_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True
        
        n = len(nums)
        count = 0

        for start in range(n):
            for end in range(start, n):
                subarray = nums[start:end + 1]
                diff_array = nums[:start] + nums[end + 1:]
                if is_strictly_increasing(diff_array):
                    count += 1

        return count
