class Solution:
    #O(N) space
    def productExceptSelf(self, nums):
        nums_size = len(nums) 
        prefix_prod = [1] 
        suffix_prod = [1] * (nums_size+1)
        res = []
        for i in range(0 , nums_size):
            val = prefix_prod[i] * nums[i]
            prefix_prod.append(val)

        for i in range(nums_size-1 ,-1 , -1):               
            val = suffix_prod[i+1] * nums[i]
            suffix_prod[i] = val

        print(prefix_prod , suffix_prod)

        for i in range(0 , nums_size):
            res.append(prefix_prod[i] * suffix_prod[i+1])
        return res
        
    #O(1) space
    def productExceptSelf(self, nums):
        product =1
        cnt_zeroes = 0
        product_non_zeroes = 1
        res = [0] * (len(nums))
        for ele in nums:
            product *= ele
            if ele == 0:
                cnt_zeroes +=1
            else:
                product_non_zeroes *= ele
            
        if product != 0 :
            for i in range (0 , len(nums)):
                res[i] = int(product/nums[i])
            return res
        elif(cnt_zeroes == 1):
            for i in range (0 , len(nums)):
                if nums[i] == 0:
                    res[i] = int(product_non_zeroes)
            return res
        else:
            #pass
            # do nothing
            return nums



print(Solution().productExceptSelf([9 , 0 ,-2]))