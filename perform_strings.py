class Solution:
    def stringShift(self, s, shift):
        move_left = 0
        length_of_string = len(s)
        for direction , amount in shift:
            print('dir , amt :: ' , direction , amount)
            if direction == 0:
                move_left = move_left + amount
                print('dir -> 0:: ' , move_left)
            else:
                move_left -= amount
                print('dir -> else block:: ' , move_left)
        print('move left:: ' , move_left)      
        print('move left , len s:: ' , move_left , length_of_string , move_left % length_of_string)  
        move_left = move_left % length_of_string
        

        return s[move_left:] + s[:move_left]
            
            
            
#print(Solution().stringShift('abc' , [[0,1],[1,2]]))

print(Solution().stringShift('abcdefg' , [[1,1],[1,1],[0,2],[1,3]]))