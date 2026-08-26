class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            found = False
            index = nums2.index(n)

            for x in nums2[index+1:]:
                if x > n:
                    result.append(x)
                    found=True
                    break
                
            if found==False:
                result.append(-1)
        return result
                
                