class Solution:
    #def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums) -> None:
        mod = []
        ctr = 0
        for ele in nums:
            if(ele != 0):
                mod.append(ele)
            else:
                ctr += 1
                
        for i in range(0 , ctr):
            print(ctr)
            mod.append(0)
        print(mod)

        

    def moveZeroes1(self, nums) -> None:
        zeroes = 0
        end_index = 0
        for ele in nums:
            if(ele == 0):
                zeroes += 1
            else:
                nums[end_index] = ele
                end_index += 1
            
        for _ in range(zeroes):
            nums[end_index] = 0
            end_index += 1

    def moveZeroes2(self, nums) -> None:
        num_zeroes = nums.count(0)

        if not num_zeroes:
            return

        nums[:] = [x for x in nums if x != 0]
        
        nums.extend([0] * num_zeroes)
        print(nums)

    """
    for i, e in reversed(list(enumerate(nums))):
            if e == 0:
                nums.append(nums.pop(i))
    """
       

if __name__ == "__main__":
    n = [0,1,0,3,12]
    #n = [0,1]
    Solution().moveZeroes2(n)