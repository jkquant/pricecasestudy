import unittest
from yobota_price import Loan
from math import pi
import datetime

class TestCases(unittest.TestCase):
    #test function if it handles improper inputs correctly
    d = datetime.date(2018, 10, 11)
    
    def test_type(self):
        #loan1 = Loan(10000, 13, 5, '2018-10-11', 1) 
        # Make sure value errors are raised when necessary
        self.assertRaises(TypeError,lambda:Loan(10000, 13, 5, '2018-10-11', 1) )
        self.assertRaises(TypeError,lambda:Loan('cash', 13, 5, '2018-10-11', 1) )
        self.assertRaises(TypeError,lambda:Loan(20000, 12, 'rate', datetime.date(2018, 10, 11), 1) )
        self.assertRaises(TypeError,lambda:Loan('money', 12, 10, datetime.date(2018, 10, 11), 1) )

    def test_values(self):
        #loan1 = Loan(10000, 13, 5, '2018-10-11', 1) 
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError,lambda:Loan(10000, 1.5, 5, '2018-10-11', 1) )
        self.assertRaises(ValueError,lambda:Loan(20000, -4, 5, '2018-10-11', 1) )
