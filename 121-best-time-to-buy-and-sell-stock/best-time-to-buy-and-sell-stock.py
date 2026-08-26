class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sell = max(sell, (prices[i]-buy))

        return sell

        