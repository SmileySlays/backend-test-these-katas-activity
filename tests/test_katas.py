import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(3, 4), 7)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 4), 20)

    def test_power(self):
        self.assertEqual(katas.power(2, 8), 256)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(7), 8)


if __name__ == '__main__':
    unittest.main()
