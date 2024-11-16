namespace Solutions.hard._32_longest_valid_parentheses;

public class Solution32 {

    //O(n^2)
    //accepted - beats 29% time 6% memory
    public int LongestValidParentheses(string input) {
        if (input.Length == 0) return 0;
        int[] positions = new int[input.Length];

        var stack = new Stack<Tuple<int, char>>();
        for (int i = 0; i < input.Length; i++) {
            if (input[i] == '(') {
                stack.Push(Tuple.Create(i, input[i]));
            }
            else if (stack.Count > 0 && (input[i] == ')' && stack.Peek().Item2 == '(')) {
                var previous = stack.Pop();
                positions[previous.Item1] = 1;
                positions[i] = 1;
            }
        }

        var max = 0;
        var count = 0;
        foreach (var item in positions) {
            if (item == 1) {
                count++;
            }
            else {
                if (count > max) { max = count; }
                count = 0;
            }
        }

        return (count > max) ? count : max;
    }

    public int LongestValidParenthesesInProgress(string input) {
        if (input.Length == 0) return 0;
        var validList = new List<int>();

        var stack = new Stack<Tuple<int, char>>();
        var longestNumber = 0;
        for (int i = 0; i < input.Length; i++) {
            char brace = input[i];
            if (stack.Count == 0 && brace == '(') {
                stack.Push(Tuple.Create(i, brace));
            }
            else if (stack.Peek().Item2 == '(' && brace == ')') {
                stack.Pop();
                longestNumber += 2;
            }
            else if (stack.Peek().Item2 == '(') {
                stack.Push(Tuple.Create(i, brace));
            }
            else {
                stack.Clear();
                validList.Add(longestNumber);
                longestNumber = 0;
            }
        }
        validList.Add(longestNumber);

        return validList.Max();
    }
}
