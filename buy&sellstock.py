class Solution:
    #def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices) -> int:
        print(prices)
        if not prices:
            return 0
        
        profit = 0
        for i in range(0 , len(prices) - 1):
            print("p " , prices[i] ," : ", prices[i + 1])
            if(prices[i + 1] > prices[i]):
                profit += prices[i + 1] - prices[i]
                print("profit " , profit)
        return profit
            
        
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))