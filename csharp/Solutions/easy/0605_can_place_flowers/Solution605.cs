namespace Solutions.easy._0605_can_place_flowers;

public class Solution605 {

    //accepted - beats 99% time and 85% mem
    //O(n)
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;
        int flowersLeft = n;
        int left = -1;
        int right = -1;

        for (int i = 0; i < flowerbed.Length; i++) {
            left = i - 1 >= 0 ? flowerbed[i - 1] : flowerbed[i];
            right = i + 1 < flowerbed.Length ? flowerbed[i + 1] : flowerbed[i];

            if (left == 0 && flowerbed[i] == 0 && right == 0) {
                flowerbed[i] = 1;
                flowersLeft--;
            }
            if (flowersLeft == 0) return true;
        }
        return flowersLeft == 0;
    }

    //Official Optimized solution
    //just like unoptimized but stops when all flowers are planted
    //pretty much the same as above

    //C++ implementation

    //class Solution {
    //    public:
    //bool canPlaceFlowers(vector<int>& flowerbed, int n) {
    //        int count = 0;
    //        for (int i = 0; i < flowerbed.size(); i++) {
    //            // Check if the current plot is empty.
    //            if (flowerbed[i] == 0) {
    //                // Check if the left and right plots are empty.
    //                bool emptyLeftPlot = (i == 0) || (flowerbed[i - 1] == 0);
    //                bool emptyRightPlot = (i == flowerbed.size() - 1) || (flowerbed[i + 1] == 0);

    //                // If both plots are empty, we can plant a flower here.
    //                if (emptyLeftPlot && emptyRightPlot) {
    //                    flowerbed[i] = 1;
    //                    count++;
    //                    if (count >= n) {
    //                        return true;
    //                    }
    //                }
    //            }
    //        }
    //        return count >= n;
    //    }
    //};
}
