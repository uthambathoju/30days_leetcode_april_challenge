import itertools
class Solution:
    def backspaceCompare1(self, S, T) -> bool:
       S_stack = []
       #for i in range(0 , len(list(S)):
       for ele in list(S):
           if(ele !='#'):
               S_stack.append(ele)
           elif(len(S_stack) != 0):
                S_stack.pop()

       T_stack = []
       for ele in list(T):
           if(ele !='#'):
               T_stack.append(ele)
           elif(len(T_stack) != 0):
               T_stack.pop()
            
       if(str(S_stack) == str(T_stack)):
           return True
       else:
           return False


    def backspaceCompare2(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))

    def backspaceCompare(self, S, T):
        print(S , T)
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            print( i , j )
            while i >= 0 and (backS or S[i] == '#'):
                print("i value " , i , " :: " , backS , " :: " , S[i])
                backS += 1 if S[i] == '#' else -1
                print("i value after" , i , " :: " , backS , " :: " , S[i])
                i -= 1
            print("final i " , i)
            while j >= 0 and (backT or T[j] == '#'):
                print("j value " , j , " :: " , backT , " :: " , T[j])
                backT += 1 if T[j] == '#' else -1
                print("j value after" , j , " :: " , backT , " :: " , T[j])
                j -= 1
            print("final j " , j)
            print(S , T)
            print( i , j , S[i] , T[j])
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                print("in if  value " , i , j ,  " :: " , S[i] , " :: " , T[j])
                return i == j == -1

            i, j = i - 1, j - 1

            
        






if __name__ == '__main__':
    #print(Solution().backspaceCompare("ab#c" , "ad#c"))
    #print(Solution().backspaceCompare("ab##" , "c#d#"))
    #print(Solution().backspaceCompare("a##c" , "#a#c"))
    print(Solution().backspaceCompare("a#c" , "b"))

    i = 2
    if not (i >= 0):
        print('yes')
    else:
        print('no')