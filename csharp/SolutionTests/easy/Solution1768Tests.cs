using NUnit.Framework;
using Solutions.easy._1768_merge_strings_alternately;

namespace SolutionTests.easy; 

[TestFixture]
internal class Solution1768Tests {
    private Solution1768 _cut;

    [SetUp]
    public void SetUp() {
        _cut = new Solution1768();
    }

    [Test]
    public void MergeAlternately_ShallReturnAlternatedMergeOfTwoStrings_WhenTwoStringsAreEqualLength() {
        var word1 = "abc";
        var word2 = "pqr";
        var actual = _cut.MergeAlternately(word1, word2);
        var expected = "apbqcr";
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void MergeAlternately_ShallReturnAlternatedMergeOfTwoStrings_WhenWord1IsShorter() {
        var word1 = "ab";
        var word2 = "pqrs";
        var actual = _cut.MergeAlternately(word1, word2);
        var expected = "apbqrs";
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void MergeAlternately_ShallReturnAlternatedMergeOfTwoStrings_WhenWord2IsShorter() {
        var word1 = "abcd";
        var word2 = "pq";
        var actual = _cut.MergeAlternately(word1, word2);
        var expected = "apbqcd";
        Assert.That(actual, Is.EqualTo(expected));
    }

    [Test]
    public void MergeAlternately_ShallReturnAlternatedMergeOfTwoStrings_WhenBothWordsAreSingleLetter() {
        var word1 = "a";
        var word2 = "b";
        var actual = _cut.MergeAlternately(word1, word2);
        var expected = "ab";
        Assert.That(actual, Is.EqualTo(expected));
    }


}
