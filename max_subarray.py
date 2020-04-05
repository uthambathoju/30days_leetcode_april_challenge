from sys import maxsize
class Solution:
    def maxSubArray(self, nums) -> int:
        max_end_here = 0
        max_so_far = 0
        for ele in nums:
            print("ele " , ele)
            max_end_here = max_end_here + ele
            print("first :: " , max_end_here)
            if(max_end_here < 0):
                print("end :: " , max_so_far)
                max_end_here = 0
            elif(max_so_far < max_end_here):
                print("far :: " , max_so_far)
                max_so_far = max_end_here
            
        return max_so_far
    
    #for all negative numbers
    def maxSubArray2(self, nums) -> int:
        max_end_here = nums[0]
        max_so_far = nums[0]
        for i in range(1 , len(nums)):
            curr_max = max(nums[i] , max_end_here + nums[i])
            print(curr_max)
            max_end_here = nums[i]
            #max_so_far = max(max_so_far , curr_max)
            if (max_so_far < curr_max):
                max_so_far = curr_max
                
            print("far :: " , max_so_far)
        return max_so_far
        

    def maxSubArray2(self, nums) -> int:
        max_end_here = nums[0]
        max_so_far = nums[0]
        for i in range(1 , len(nums)):
            curr_max = max(nums[i] , max_end_here + nums[i])
            print(curr_max)
            max_end_here = nums[i]
            #max_so_far = max(max_so_far , curr_max)
            if (max_so_far < curr_max):
                max_so_far = curr_max
                
            print("far :: " , max_so_far)
        return max_so_far

    def maxSubArray3(self, nums) -> int:
        ans = 0
        a = 0
        for ele in nums:
            a +=ele
            ans = max(ans , a)
            a = max(a ,0)
        return ans
    
    def maxSubArray4(self, nums):
        max_so_far = -maxsize - 1
        print("val " , max_so_far)
        max_ending_here = 0
        for i in range(0, len(nums)): 
            print("num :: " , nums[i])
            max_ending_here = max_ending_here + nums[i] 
            print("end " , max_ending_here)
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
                print("far " , max_so_far)
            if max_ending_here < 0: 
                 max_ending_here = 0   
        return max_so_far 
        
    def maxSubArray6(self, nums) -> int:
        max_end_here = 0
        max_so_far = -10000
        for ele in nums:
            max_end_here = max_end_here + ele
            if(max_so_far < max_end_here):
                max_so_far = max_end_here	
            
            if(max_end_here < 0):
                max_end_here = 0
            
            
        return max_so_far
		

if __name__ == "__main__":
    #n = [-2,1,-3,4,-1,2,1,-5,4]
    n = [-2 ,-1]
    sol = Solution()
    print(sol.maxSubArray6(n))

