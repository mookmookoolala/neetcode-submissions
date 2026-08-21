class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for i,n in enumerate(nums2):
            mapping[n] = i
        
        result = []
        for n in nums1:
            result.append(mapping[n])
        return result
                