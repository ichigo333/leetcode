using NUnit.Framework;
using Solutions.easy._1431_kids_with_the_greatest_number_of_candies;

namespace SolutionTests.easy;

[TestFixture]
internal class Solution1431Tests {
    private Solution1431 _cut;

    [SetUp]
    public void SetUp() {
        _cut = new Solution1431();
    }

    [Test]
    public void KidsWithCandies_ShallReturnAllExceptIndexThree_WhenIndexThreeIsNotGreatest() {
        bool[] expected = [true, true, true, false, true];
        int[] candies = [2, 3, 5, 1, 3];
        var actual = _cut.KidsWithCandies(candies, 3);
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void KidsWithCandies_ShallReturnTrueOnlyForIndexZero_WhenExtraCandiesIsOne() {
        bool[] expected = [true, false, false, false, false];
        int[] candies = [4, 2, 1, 1, 2];
        var actual = _cut.KidsWithCandies(candies, 1);
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void KidsWithCandies_ShallReturnForTwoOfTheThree_WhenFirstAndLastIsGreatesAndEqual() {
        bool[] expected = [true, false, true];
        int[] candies = [12, 1, 12];
        var actual = _cut.KidsWithCandies(candies, 10);
        Assert.That(actual, Is.EqualTo(expected));
    }

}
