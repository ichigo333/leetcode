namespace Solutions;

public class Solution20 {
    // Accepted - beats 98% time 35% mem
    public bool IsValid(string input) {
        if (input.Length % 2 != 0) return false;

        var stack = new Stack<char>();
        foreach (char brace in input) {
            if (brace == '(' || brace == '[' || brace == '{') { stack.Push(brace); }
            else if (stack.Count > 0 &&
                ((stack.Peek() == '(' && brace == ')') ||
                (stack.Peek() == '{' && brace == '}') ||
                (stack.Peek() == '[' && brace == ']'))) {
                stack.Pop();
            }
            else
                return false;
            }
        return stack.Count == 0;
     }

    // Accepted - beats 30% time 29% mem
    public bool IsValidFirstAttempt(string input) {
        var braceDict = new Dictionary<char, char> {
            { '(', ')' },
            { '[', ']' },
            { '{', '}' }
        };

        if (input.Length % 2 != 0) return false;
        if (braceDict.ContainsValue(input[0])) return false;

        var stack = new Stack<char>();
        foreach (char brace in input) {
            if (braceDict.ContainsKey(brace)) { stack.Push(brace); }
            else if (stack.Count != 0 && braceDict[stack.Peek()] == brace) { stack.Pop(); }
            else { return false; }
        }

        return stack.Count == 0;
    }
}
