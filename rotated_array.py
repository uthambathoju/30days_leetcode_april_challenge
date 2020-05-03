class Solution:
    def search(self, nums, target: int) -> int:
        nums_size = len(nums)
        if nums is None or nums_size == 0:
            return -1
        
        left = 0
        right = nums_size -1
        while(left < right):
            midpoint = int(left + (right - left) / 2)
            print("midpoint , left , right :: " , midpoint , " , " , left , " , " , right)
            if(nums[midpoint] > nums[right]):
                left = midpoint + 1
                print(" in if :: " ,nums[midpoint] , " , " , nums[right], " :: " , left)
            else:
                right = midpoint
                print(" in else :: " ,nums[midpoint] , " , " , nums[right] , " :: " , right)

        print("left and right  :: " , left , right )
        start = left
        left = 0
        right = nums_size -1

        if target >= nums[start] and target <= nums[right]:
            left = start
            print(" target in if :: " , left , " :: start :: " , right)
        else:
            right = start
            print(" target in else :: " , right)
        
        while(left <= right):
            midpoint = int(left + (right - left)/ 2)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1 



 



print(Solution().search([4,5,6,7,0,1,2] , 0))