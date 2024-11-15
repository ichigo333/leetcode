using System.Text;

namespace Solutions.easy._1768_merge_strings_alternately; 

public class Solution1768 {

    //accepted - 53% time 99% memory
    //O(n)
    public string MergeAlternately(string word1, string word2) {
        var result = new StringBuilder();
        int maxLength = Math.Max(word1.Length, word2.Length);

        for (var index = 0; index < maxLength; index++) {
            if (index < word1.Length) {
                result.Append(word1[index]);
            }

            if (index < word2.Length) {
                result = result.Append(word2[index]);
            }
        }
        return result.ToString();
    }

    //accepted - 46% time 94% memory
    //with while loop
    public string MergeAlternatelyAttempt2(string word1, string word2) {
        var result = new StringBuilder();
        var index = 0;

        while (index < word1.Length || index < word2.Length) {
            if (index < word1.Length) {
                result.Append(word1[index]);
            }

            if (index < word2.Length) {
                result = result.Append(word2[index]);
            }
            index++;
        }
        
        return result.ToString();
    }

    //Solution from comments
    //beats 80% time and 34% memory
    public string MergeAlternatelySolution(string word1, string word2) {
        string result = "";
        int w1 = word1.Length;
        int w2 = word2.Length;
        int i = 0;
        int j = 0;
        while (i < w1 && j < w2) {
            result += word1[i];
            result += word2[j];
            i++;
            j++;
        }

        while (i < w1) {
            result += word1[i];
            i++;
        }

        while (j < w2) {
            result += word2[j];
            j++;
        }

        return result;
    }
}
