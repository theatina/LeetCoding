class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    median = None
    
    final_list = nums1+nums2
    final_list.sort()
    
    middle = len(final_list)//2
    if (len( final_list)/2).is_integer():
        median = (final_list[middle-1]+final_list[middle])/2
    else:
        median = final_list[middle]
            
    return median