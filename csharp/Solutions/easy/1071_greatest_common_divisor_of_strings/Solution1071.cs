using System.Numerics;

namespace Solutions.easy._1071_greatest_common_divisor_of_strings;

public class Solution1071 {

    //accepted - 100% time 38% memory
    //O(m+n)?
    //possibly O(min(m,n)⋅(m+n))
    public string GcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) { return ""; }

        var str1Length = str1.Length;
        var str2Length = str2.Length;
        var minLength = Math.Min(str1Length, str2Length);

        for (var i = minLength; i > 0; i--) {
            if ((str1Length % i == 0 && str2Length % i == 0)
                && str1[..i] == str2[..i]) {
                    return str1[..i];
            }
        }
           
        return "";
    }


    //Official solution - using a library for some god damn reason
    //converted from C++ below
    //O(m+n)
    public string GcdOfStringsOfficial(string str1, string str2) {
        // Check if they have non-zero GCD string.
        if (str1 + str2 != str2 + str1) {
            return "";
        }

        // Get the GCD of the two lengths.
        var gcdLength = BigInteger.GreatestCommonDivisor(str1.Length, str2.Length);
        return str1.Substring(0, (int)gcdLength);
    }

    //Official C++ version
    //class Solution {
    //    public:
    //string gcdOfStrings(string str1, string str2) {
    //        // Check if they have non-zero GCD string.
    //        if (str1 + str2 != str2 + str1) {
    //            return "";
    //        }

    //        // Get the GCD of the two lengths.
    //        int gcdLength = gcd(str1.size(), str2.size());
    //        return str1.substr(0, gcdLength);
    //    }
    //};
}
