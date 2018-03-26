import unittest
from prime import is_prime

class primeTesting(unittest.TestCase):
    def test_for_prime(self):
        """ Is a prime number successfully determined prime? """
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        for number in prime_numbers:
            self.assertTrue(is_prime(number), "Failed test for {}".format(number))

    def test_for_no_prime(self):
        """ Is a prime number successfully determined prime? """
        prime_numbers = [4, 6, 8, 10, 12, 14, 16]
        for number in prime_numbers:
            self.assertFalse(is_prime(number), "Failed test for {}".format(number))

    def test_for_special(self):
        """ Is a prime number successfully determined prime? """
        special_numbers = [0, 1]
        for number in special_numbers:
            self.assertFalse(is_prime(number), "Failed test for {}".format(number))

    def test_for_negative(self):
        """ Is a prime number successfully determined prime? """
        negative_numbers = [-1, -2, -3, -4, -5, -6]
        for number in negative_numbers:
            self.assertFalse(is_prime(number), "Failed test for {}".format(number))
def main():
    unittest.main()
if __name__ == "__main__":
    main()

