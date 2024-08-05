import unittest
from client3 import getDataPoint, getRatio

class Client3Test(unittest.TestCase):

    def test_getDataPoint(self):
        quote = {
            'stock': 'ABC',
            'top_bid': {'price': 120.48},
            'top_ask': {'price': 121.2}
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 121.2)
        self.assertEqual(price, (120.48 + 121.2) / 2)

    def test_getDataPoint_with_different_data(self):
        quote = {
            'stock': 'DEF',
            'top_bid': {'price': 130.48},
            'top_ask': {'price': 131.2}
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'DEF')
        self.assertEqual(bid_price, 130.48)
        self.assertEqual(ask_price, 131.2)
        self.assertEqual(price, (130.48 + 131.2) / 2)

    def test_getRatio(self):
        price_a = 120.48
        price_b = 121.2
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, price_a / price_b)

        price_b = 0
        ratio = getRatio(price_a, price_b)
        self.assertIsNone(ratio)

    def test_getRatio_with_zero_prices(self):
        price_a = 0
        price_b = 0
        ratio = getRatio(price_a, price_b)
        self.assertIsNone(ratio)

if __name__ == "__main__":
    unittest.main()