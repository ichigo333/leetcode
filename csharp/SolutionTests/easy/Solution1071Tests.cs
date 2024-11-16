using NUnit.Framework;
using Solutions.easy._1071_greatest_common_divisor_of_strings;

namespace SolutionTests.easy;

[TestFixture]
internal class Solution1071Tests {
    private Solution1071 _cut;

    [SetUp]
    public void SetUp() {
        _cut  = new Solution1071();
    }

    [Test]
    public void GcdOfStrings_ShallReturnStr2_WhenBothAreDivisibleByStr2() {
        var string1 = "ABCABC";
        var string2 = "ABC";
        var actual = _cut.GcdOfStrings(string1, string2);
        var expected = "ABC";
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void GcdOfStrings_ShallReturnAB_WhenStr1CannotBeFullyDividedByStr2() {
        var string1 = "ABABAB";
        var string2 = "ABAB";
        var actual = _cut.GcdOfStrings(string1, string2);
        var expected = "AB";
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void GcdOfStrings_ShallReturnEmptyString_WhenStringsAreNotDivisible() {
        var string1 = "LEET";
        var string2 = "CODE";
        var actual = _cut.GcdOfStrings(string1, string2);
        var expected = "";
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void GcdOfStrings_ShallReturnEmptyAB_WhenBothStringsAreAB() {
        var string1 = "AB";
        var string2 = "AB";
        var actual = _cut.GcdOfStrings(string1, string2);
        var expected = "AB";
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void GcdOfStrings_ShallReturnEmptyABC_WhenOnlyABCMatches() {
        var string1 = "ABCDEF";
        var string2 = "ABC";
        var actual = _cut.GcdOfStrings(string1, string2);
        var expected = "";
        Assert.That(actual, Is.EqualTo(expected));
    }
}
