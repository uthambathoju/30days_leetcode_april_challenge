#from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        print("length : " , N)
        #@lru_cache(None)
        def isValidString(index , balance):
            print(" index , balance :: " , index , " , " , balance)
            if(index == N):
                print(" length equal ")
                if(balance == 0):
                    return True
                else:
                    print(" length equal failed")
                    return False
                
            if(balance < 0):
                print(" length equal less")
                return False
                
                
            if(s[index] == '('):
                print("here (")
                return isValidString(index + 1 , balance + 1)
            elif(s[index] == ')'):
                print("here )")
                return isValidString(index + 1 , balance - 1)
            else:
                print("in * function call ")
                return isValidString(index + 1 , balance - 1) or isValidString(index + 1 , balance + 1) or isValidString(index + 1 , balance)

        print("here")
        return isValidString(0 ,0)
                    

#print(Solution().checkValidString('((())*)'))
print(Solution().checkValidString('(*)'))
