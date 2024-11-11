namespace Solutions.easy._121_best_time_to_buy_and_sell_stock; 

public class Solution121 {

    //accepted - time 100% mem 54%
    //Complexity: O(n) & Space O(1)
    //two pointers algorithm / also sliding window?
    public int MaxProfit111(int[] prices) {
        var left = prices[0];
        var right = 0;
        var maxProfit = 0;
        for (var i = 1; i < prices.Length; i++) {
            right = prices[i];
            if (left > right) {
                left = right;
            }
            else if (right - left > maxProfit) {
                maxProfit = right - left;
            }
        }

        return maxProfit;
    }

    //Dynamic Programming solution
    //Complexity: O(n) & Space O(1)
    public int MaxProfit(int[] prices) {
        int minPrice = int.MaxValue;
        int maxProfit = 0;

        foreach (int currentPrice in prices) {
            minPrice = Math.Min(currentPrice, minPrice);
            maxProfit = Math.Max(maxProfit, currentPrice - minPrice);
        }

        return maxProfit;
    }
}
