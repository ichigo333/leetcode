namespace Solutions.easy._1431_kids_with_the_greatest_number_of_candies;

public class Solution1431 {

    //accepted - beats 60% time and 49% mem
    //attempt1 - brute force
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        bool[] result = new bool[candies.Length];

        for (int i = 0; i < candies.Length; i++) {
            var currentMax = candies[i] + extraCandies;
            var isMax = true;
            for (int j = 0; j < candies.Length; j++) {
                if (candies[j] > currentMax) { isMax = false; break; }
            }
            result[i] = isMax;
        }

        return result;
    }

    //official - somehow worse?
    //beats 56% time and 59% mem
    public IList<bool> KidsWithCandiesOfficial(int[] candies, int extraCandies) {
        bool[] result = new bool[candies.Length];
        var maxCandies = candies.Max();

        for (int i = 0; i < candies.Length; i++) {
            result[i] = candies[i] + extraCandies >= maxCandies;
        }
            
        return result;
    }
}
