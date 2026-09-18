class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}; # target, index
        goal = [];            

        for j in range(len(nums)):
            if target-nums[j] in pairs: #runtime of in = O(1)
                goal.append(pairs[target-nums[j]])
                goal.append(j)
                break;
            else:
                pairs[nums[j]] = j ;
        return goal

