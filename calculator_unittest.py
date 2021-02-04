import unittest
import math

import calculator

class test_calculator(unittest.TestCase):

    def test_operations(self):
        self.assertEqual(calculator.calc(5,10), (15,-5,50,0.5))

    def test_pos_div_0(self):
        self.assertEqual(calculator.calc(10,0), (10,10,0,math.inf))

    def test_neg_div_0(self):
        self.assertEqual(calculator.calc(-10,0), (-10,-10,0,-math.inf))

    def test_accept_str_int(self):
        self.assertEqual(calculator.calc("5", "10"), (15,-5,50,0.5))

    def test_decline_str(self):
        self.assertEqual(calculator.calc("words", "ints"), math.inf)

if __name__ == '__main__':
    unittest.main()
