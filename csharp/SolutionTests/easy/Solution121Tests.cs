using NUnit.Framework;
using Solutions.easy._121_best_time_to_buy_and_sell_stock;

namespace SolutionTests.easy;

[TestFixture]
internal class Solution121Tests {
    private Solution121 _cut;

    [SetUp]
    public void SetUp() {
        _cut = new Solution121();
    }

    [Test]
    public void MaxProfit_ShallReturn5_WhenOneAndSixAreBestPricesToBuyAndSell() {
        int[] prices = [7, 1, 5, 3, 6, 4];
        var actual = _cut.MaxProfit(prices);
        Assert.That(actual, Is.EqualTo(5));
    }

    [Test]
    public void MaxProfit_ShallReturn0_WhenTransactionNotPossible() {
        int[] prices = [7, 6, 4, 3, 1];
        var actual = _cut.MaxProfit(prices);
        Assert.That(actual, Is.EqualTo(0));
    }

    [Test]
    public void MaxProfit_ShallReturn20_WhenBestPriceDifferenceIsFirst() {
        int[] prices = [20, 40, 1, 2];
        var actual = _cut.MaxProfit(prices);
        Assert.That(actual, Is.EqualTo(20));
    }

    [Test]
    public void MaxProfit_ShallReturn20_ThereAreTwoNumbersOnly() {
        int[] prices = [20, 40];
        var actual = _cut.MaxProfit(prices);
        Assert.That(actual, Is.EqualTo(20));
    }

    [Test]
    public void MaxProfit_ShallReturn0_ThereAreTwoNumbersOnlyAndLargerOnLeft() {
        int[] prices = [40, 20];
        var actual = _cut.MaxProfit(prices);
        Assert.That(actual, Is.EqualTo(0));
    }

    [Test]
    public void MaxProfit_ShallReturn0_IfThereIsOnlyOneNubmer() {
        int[] prices = [40];
        var actual = _cut.MaxProfit(prices);
        Assert.That(actual, Is.EqualTo(0));
    }

    [Test]
    public void MaxProfit_ShallReturn20_IfThereCombinationIsAtTheEnd() {
        int[] prices = [7, 5, 3, 6, 4, 1, 40];
        var actual = _cut.MaxProfit(prices);
        Assert.That(actual, Is.EqualTo(39));
    }
}
