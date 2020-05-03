import collections
class Solution:
    def findMaxLength1(self, nums) -> int:
        print(nums)
        res = 0
        idx = 0
        chk_lst = []
        while(idx < len(nums)):
            bin_ctr = 1
            check_val = nums[idx]
            print("chek ", idx)
            for i in range(idx + 1 , len(nums)):
                if(nums[i] == check_val):
                    bin_ctr +=1
                else:
                    break
            sub_idx = bin_ctr+bin_ctr
            print("idx " , idx)
            sub_arr = nums[bin_ctr:bin_ctr+bin_ctr]
            print("sub_arr :" , sub_arr)
            
            print("lst :" , chk_lst)
            if check_val == 0 :
                if(sub_arr.count(1) == bin_ctr and len(chk_lst) == 0 and sub_arr != chk_lst):
                    print(sub_arr , " :: " ,chk_lst , " :: " ,sub_idx)
                    res +=sub_idx
            else:        
                if(sub_arr.count(0) == bin_ctr and  len(chk_lst) == 0 and sub_arr != chk_lst):
                    print("else :: " ,sub_arr , " :: " ,chk_lst , " :: " ,sub_idx)
                    res +=1
            
            if sub_arr not in chk_lst:
                chk_lst.append(sub_arr)
            idx += 1
        return res
            

    def findMaxLength(self, nums) -> int:
            dict_subarr = collections.defaultdict(int)
            max_length = 0
            count = 0
            dict_subarr[0] = -1
            for i in range(0 ,  len(nums)):
                print("ele  :: " , nums[i])
                if nums[i] == 0:
                     count -= 1 
                else:
                     count += 1 
                print("count value  :: " , count)

                if(count in dict_subarr.keys()):
                    print("dict keys  :: " , dict_subarr.keys())
                    print("dict vals  :: " , dict_subarr.values())
                    print("max_length  :: " , max_length)
                    print("vallll   :: , iteration num  ", i ," :: " , "key  ::" ,count , ":: dict ", dict_subarr[count] ,"sub ::" , i- dict_subarr[count])
                    max_length = max(max_length , i-dict_subarr[count])
                    
                else:
                    dict_subarr[count] = i
            return max_length







print(Solution().findMaxLength([0,1,0,0,1,1,0]))