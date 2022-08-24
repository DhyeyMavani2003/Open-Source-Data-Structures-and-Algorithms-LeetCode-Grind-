class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        a=nums1+nums2
        a.sort()
        l=len(a)
        if l%2==0:
            return (a[int(l/2)]+a[int((l/2)-1)])/2
        else:
            return a[int(l/2)]