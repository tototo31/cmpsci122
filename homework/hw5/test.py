import unittest
from HW5 import isPalindrome


class PalidromeTestCases(unittest.TestCase):
    """Tests for HW5.py"""

    #Write your test cases here 
    def test_palindromes(self):
        palinList = ["alula", "Madam", "Mr. Owl ate my metal worm", "Live on time, emit no evil", "Step on no pets", "Cigar? Toss it in a can. It is so tragic.", "Yen o' money."]
        for palin in palinList:
            print("TESTING KNOWN PALINDROME {}".format(palin))
            self.assertTrue(isPalindrome(palin), "{} incorectly classed as a Non-Palindrome".format(palin))

    def test_notPalindromes(self):
        nonPalinList = ["love", 12, 11, 12.5, 12.21, [12,21], "travel.. a town in Alaska"]
        for nonPalin in nonPalinList:
            print("TESTING KNOWN NON-PALINDROME {}".format(nonPalin))
            self.assertFalse(isPalindrome(nonPalin), "{} incorrectly classed as a palindrome".format(nonPalin))

    #Your test cases end

#Do NOT modify this part. Include it in your submission
if __name__ == '__main__':
    def results():
        t = unittest.main(exit=False)
        tests=t.result.testsRun
        fail= len(t.result.failures)
        error=len(t.result.errors)
        final=tests-fail-error
        print(tests,fail,final)
        return tests,fail,final
    results()
