class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    median = None
    
    final_list = nums1+nums2
    final_list.sort()
    
    if (len( final_list)/2).is_integer():
        median = (final_list[len(final_list)//2-1]+final_list[len(final_list)//2])/2
    else:
        median = final_list[len(final_list)//2]
            
    return median