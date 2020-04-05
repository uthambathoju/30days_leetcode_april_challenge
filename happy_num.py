class Solution:
    def split_squared(self , n:int) -> int:
        sum = 0
        for digit in str(n):
            sum += int(digit) ** 2
        return sum 

    def split_squared2(self , n:int) -> int:
        sum = 0
        while(n > 0):
            digit = n % 10
            n = int(n / 10)
            sum += (digit) ** 2
        return sum 

    def isHappy(self, n: int) -> bool:
        checked = set()
        while(n > 1  and n not in checked):
            print(checked)
            checked.add(n)
            n = self.split_squared2(n)
            print(" SUM  " , n)
        return n == 1 
    
    def isHappy2(self, n: int) -> bool:
        count = 0
        while(n > 1  and count < 6):
            print("Hi")
            if(n < 1000):
                count += 1
            n = self.split_squared2(n)
            print("SUM  " , n)
        return n == 1 

if __name__ == '__main__':
    n = 19
    hnum = Solution()
    hnum.isHappy(n)
