"""
Тесты для калькулятора.
"""

import unittest
from calculator import add, subtract, multiply, divide, power


class TestCalculator(unittest.TestCase):
    """Тестовый класс для функций калькулятора."""
    
    def test_add(self):
        """Тест функции сложения."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -3), -8)
    
    def test_subtract(self):
        """Тест функции вычитания."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -3), 1)
        self.assertEqual(subtract(10, 10), 0)
    
    def test_multiply(self):
        """Тест функции умножения."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-3, -4), 12)
    
    def test_divide(self):
        """Тест функции деления."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Тест деления на ноль."""
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_power(self):
        """Тест функции возведения в степень."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)
        self.assertEqual(power(2, -1), 0.5)


if __name__ == '__main__':
    unittest.main()
