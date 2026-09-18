class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sol = set()
        dupe = False
        for i in range (len(nums)):
            if nums[i] in sol:
                dupe = True
                break   
            else:
                sol.add(nums[i])
        return dupe;
