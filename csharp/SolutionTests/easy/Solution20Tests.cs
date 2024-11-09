using NUnit.Framework;
using Solutions;

namespace SolutionTests.easy;

[TestFixture]
public class Solution20Tests {
    private Solution20 _cut;

    [SetUp]
    public void SetUp() {
        _cut = new Solution20();
    }

    [TestCase("()", true)]
    [TestCase("()[]{}", true)]
    [TestCase("([])", true)]
    public void isValid_ReturnsTrue_ForEvenNumberOfBrackets(string input, bool expected) {
        var actual = _cut.IsValid(input);
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void isValid_ReturnsFalse_IfOpeningBraceFollowedByDifferentClosingBrace() {
        var actual = _cut.IsValid("(]");
        Assert.That(actual, Is.EqualTo(false));
    }

    [Test]
    public void isValid_ReturnsFalse_IfNumberOfBracesIsOdd() {
        var actual = _cut.IsValid("(");
        Assert.That(actual, Is.EqualTo(false));
    }

    [Test]
    public void isValid_ReturnsFalse_IfTwoClosingBracesAtTheStart() {
        var actual = _cut.IsValid("){");
        Assert.That(actual, Is.EqualTo(false));
    }


    [Test]
    public void isValid_ReturnsFalse_IfTwoClosingBraceWithoutOpening() {
        var actual = _cut.IsValid("(){}}{");
        Assert.That(actual, Is.EqualTo(false));
    }

    [Test]
    public void isValid_ReturnsFalse_IfBracesAreOpenOnes() {
        var actual = _cut.IsValid("({[");
        Assert.That(actual, Is.EqualTo(false));
    }
}
