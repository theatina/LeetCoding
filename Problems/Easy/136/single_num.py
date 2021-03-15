from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occ_dict = Counter(nums)
        index = list(occ_dict.values()).index(1)
        return list(occ_dict.keys())[index]