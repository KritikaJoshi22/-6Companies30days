class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_array = list(enumerate(nums))
        indexed_array.sort(key= lambda x:x[1], reverse = True)
        result_array = sorted(indexed_array[:k], key= lambda x:x[0])
        return [x[1] for x in result_array]