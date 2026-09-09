class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = []
        just_count=[]
        render = []
        g=1
        f=1
        for i,n in enumerate(nums):
            count.append(g)
            g *= n

        for h,d in enumerate(reversed(nums)):
            just_count.append(f)
            f *= d
        just_count.reverse()
        
        for c,e in enumerate(nums):
            true = count[c] * just_count[c]
            render.append(true)
        return render
