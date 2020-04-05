def singleNumber(nums):
        """s
        :type nums: List[int]
        :rtype: int
        """
        
        unq_ele = set(nums)
        #print(unq_ele)   
        for val in unq_ele:
            i = 0
            for ele in nums:
                if(val == ele):
                    i += 1
            if(i == 1):
                return val
