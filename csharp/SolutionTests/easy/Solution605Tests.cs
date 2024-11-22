
using NUnit.Framework;
using Solutions.easy._0605_can_place_flowers;


namespace SolutionTests.easy;

[TestFixture]
internal class Solution605Tests {
    private Solution605 _cut;

    [SetUp]
    public void SetUp() {
        _cut = new Solution605();
    }

    [Test]
    public void CanPlaceFlowers_Example1() {
        int[] flowerbeds = [1, 0, 0, 0, 1];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 1);
        Assert.That(actual, Is.EqualTo(true));
    }

    [Test]
    public void CanPlaceFlowers_Example2() {
        int[] flowerbeds = [1, 0, 0, 0, 1];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 2);
        Assert.That(actual, Is.EqualTo(false));
    }

    [Test]
    public void CanPlaceFlowers_ShallReturnTrue_IfFlowerCanBePlantedLast() {
        int[] flowerbeds = [1, 0, 0];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 1);
        Assert.That(actual, Is.EqualTo(true));
    }

    [Test]
    public void CanPlaceFlowers_ShallReturnTrue_IfFlowerbedIsEmpty() {
        int[] flowerbeds = [0, 0, 0];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 2);
        Assert.That(actual, Is.EqualTo(true));
    }

    [Test]
    public void CanPlaceFlowers_ShallReturnTrue_IfThereIsOneFlowerbedForOneFlower() {
        int[] flowerbeds = [0];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 1);
        Assert.That(actual, Is.EqualTo(true));
    }

    [Test]
    public void CanPlaceFlowers_ShallReturnFalse_IfThereIsNoFlowerbedForOneFlower() {
        int[] flowerbeds = [1];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 1);
        Assert.That(actual, Is.EqualTo(false));
    }

    [Test]
    public void CanPlaceFlowers_ShallReturnFalse_IfFlowerCannotBePlanted() {
        int[] flowerbeds = [1, 0, 0, 1, 0];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 1);
        Assert.That(actual, Is.EqualTo(false));
    }

    [Test]
    public void CanPlaceFlowers_ShallReturnTrue_IfThereAreManyPlacesToPlant() {
        int[] flowerbeds = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 2);
        Assert.That(actual, Is.EqualTo(true));
    }

    [Test]
    public void CanPlaceFlowers_FailedOnSubmittion_ShouldActuallySetOneWhenPlanted() {
        int[] flowerbeds = [1, 0, 0, 0, 0, 1];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 2);
        Assert.That(actual, Is.EqualTo(false));
    }

    [Test]
    public void CanPlaceFlowers_FailedOnSubmittion_ShallReturnTrue_IfNIsZero() {
        int[] flowerbeds = [0, 0, 0, 0, 0, 1, 0, 0];
        var actual = _cut.CanPlaceFlowers(flowerbeds, 0);
        Assert.That(actual, Is.EqualTo(true));
    }
}
