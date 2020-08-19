import unittest
from utils.stock import get_max_profit


class TestStockPricesMaxProfit(unittest.TestCase):

    def test_case_complex(self):
        stock_prices_yesterday = [10, 7, 5, 8, 11, 4,
                                  20, 10, 1, 20, 15]
        min_buy, max_sell, max_profit = get_max_profit(stock_prices_yesterday)

        self.assertEqual(min_buy, 1)
        self.assertEqual(max_sell, 20)
        self.assertEqual(max_profit, 19)

    def test_case_simple(self):
        stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        min_buy, max_sell, max_profit = get_max_profit(stock_prices_yesterday)

        self.assertEqual(min_buy, 5)
        self.assertEqual(max_sell, 11)
        self.assertEqual(max_profit, 6)

    def test_with_duplicate_values(self):
        stock_prices_yesterday = [10, 7, 1, 1, 20, 10]
        min_buy, max_sell, max_profit = get_max_profit(stock_prices_yesterday)

        self.assertEqual(min_buy, 1)
        self.assertEqual(max_sell, 20)
        self.assertEqual(max_profit, 19)


if __name__ == '__main__':
    unittest.main()
