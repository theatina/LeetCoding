class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        median = 0.0
        
        nums1.extend(nums2)
        # nums1 = list(set(nums1))
        nums1 = [x for x in nums1 if x < 0] + [x for x in nums1 if x >= 0] 
        nums1.sort()
        
        if (len( nums1)/2).is_integer():
          middle = int(len(nums1)/2)
          median = float(nums1[middle-1]+nums1[middle])/2
        else:
          middle = int(len(nums1)/2)
          median = nums1[middle]

        
        return median