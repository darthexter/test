#!/usr/bin/python3

import unittest
import calculator

class TestCalculator(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(calculator.addnum(2,5),7)
    self.assertEqual(calculator.addnum(3,8),11)
    self.assertEqual(calculator.addnum(-5,5),0)
    self.assertEqual(calculator.addnum(-12,5),-7)
  
  def test_subtract(self):
    self.assertEqual(calculator.subnum(2,5),-3)
    self.assertEqual(calculator.subnum(8,1),7)
    self.assertEqual(calculator.subnum(-2,5),-7)
    self.assertEqual(calculator.subnum(2,-5),7)

  def test_multiply(self):
    self.assertEqual(calculator.multnum(2,5),10)
    self.assertEqual(calculator.multnum(8,1),8)
    self.assertEqual(calculator.multnum(-2,5),-10)
    self.assertEqual(calculator.multnum(-2,-5),10)

  def test_division(self):
    self.assertAlmostEqual(calculator.divnum(2,2),1)
    self.assertAlmostEqual(calculator.divnum(4,2),2)
    self.assertAlmostEqual(calculator.divnum(-8,2),-4)
    self.assertAlmostEqual(calculator.divnum(7,2),3.5)
    self.assertAlmostEqual(calculator.divnum(5,-6),-0.8333333333333334)
    self.assertAlmostEqual(calculator.divnum(9,18),0.5)

  
if __name__ == '__main__':
  unittest.main()
    
