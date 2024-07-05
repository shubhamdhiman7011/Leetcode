class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n=len(nums1)
        m=len(nums2)
        count=0
        for x in range(0,n):
          for y in range(0,m):
            if(nums1[x]%(nums2[y]*k)==0):
              count=count+1  
        return count      