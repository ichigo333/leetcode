using NUnit.Framework;
using Solutions.hard._32_longest_valid_parentheses;

namespace SolutionTests.hard;

[TestFixture]
public class Solution32Tests
{
    private Solution32 _cut;

    [SetUp]
    public void SetUp() {
        _cut = new Solution32();
    }

    [Test]
    public void LongestValidParentheses_ReturnsTwo_WhenStartWithOpenAndHasOpenCloseAfter() {
        var actual = _cut.LongestValidParentheses("(()");
        Assert.That(actual, Is.EqualTo(2));
    }

    [Test]
    public void LongestValidParentheses_ReturnsFour_WhenThereAreFourInBetweenTwoInvalid() {
        var actual = _cut.LongestValidParentheses(")()())");
        Assert.That(actual, Is.EqualTo(4));
    }

    [Test]
    public void LongestValidParentheses_ReturnsZero_WhenInputIsEmpty() {
        var actual = _cut.LongestValidParentheses("");
        Assert.That(actual, Is.EqualTo(0));
    }

    [Test]
    public void LongestValidParentheses_ReturnsSix_WhenInputHasSixContinuous() {
        var actual = _cut.LongestValidParentheses("()(())");
        Assert.That(actual, Is.EqualTo(6));
    }

    [Test]
    public void LongestValidParentheses_ReturnsTwo_WhenTwoPairsAreInteruptedByInvalidBrace() {
        var actual = _cut.LongestValidParentheses("()(()");
        Assert.That(actual, Is.EqualTo(2));
    }

    [Test]
    public void LongestValidParentheses_ReturnsTwo_WhenTwoPairsAreInteruptedByTwoBrace() {
        var actual = _cut.LongestValidParentheses("()((()");
        Assert.That(actual, Is.EqualTo(2));
    }
}
