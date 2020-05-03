import collections

class Solution:
    def groupAnagrams(self, strs):
        hash_table = {}
        temp_anagrams = []
        ang_list = []
        #print(strs)
        """
        if all('' == space for space in strs):
            ang_list.append(strs)
            return ang_list
        
        str_unq = len(list(set(strs)))
        if(str_unq == 1):
            ang_list.append(strs)
            return ang_list

        """
        for ele in strs:
            hash_table[ele] = len(ele)
        #print(hash_table)
        for ele in strs:
            #print("ele :: " , ele)
            #break
            anagrams = []
            if ele not in temp_anagrams :
                listOfKeys = [key  for (key, value) in hash_table.items() if value == len(ele)]
                #anagrams.append(ele)
                #ele_chars = list(ele)
                for eq_strs in listOfKeys:
                    ctr = 0
                    #if eq_strs != ele:
                    check = list(ele)
                    if(check == ''):
                        check = ' '
                    #print("chars :: " , eq_strs)
                    for k in check:
                        #print("check :: " , check)
                        if k in eq_strs:
                            ctr += 1
                        if ctr == len(eq_strs):
                            if eq_strs == ' ':
                                anagrams.append('')
                            else:
                                anagrams.append(eq_strs)
                                #print("SUCCESS" , anagrams)
                        
            #print(" anagrams :: " , anagrams)                        
            if anagrams:
                ang_list.append(anagrams)
                temp_anagrams =  [item for sublist in ang_list for item in sublist]
                #print(" ang_list :: " , ang_list)
            #print(" temp_anagrams :: " , temp_anagrams)
        return ang_list     


    def groupAnagrams2(self , strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()      

    
    def groupAnagrams3(self, strs):
        print(strs)
        result = collections.defaultdict(list)
        for ele in strs:
            key = tuple(sorted(ele))
            result[key].append(ele)
        return result.values()
                
        
if __name__ == "__main__":
    print(Solution().groupAnagrams3(["eat", "tea", "tan", "ate", "nat", "bat"]))
    #print(Solution().groupAnagrams(["eat", "tea", "tan", "ate"]))
    #print(Solution().groupAnagrams([" ","b"]))
    