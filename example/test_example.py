import unittest
import doctest
import example

class TestFetchFortyTwo(unittest.TestCase):
    def test_fetch_forty_two(self):
        result = example.fetch_forty_two()
        expected = 42
        self.assertEqual(result,expected)

class TestFetchFortyTwoWords(unittest.TestCase):
    def test_fetch_forty_two_words(self):
        #result = example.fetch_forty_two_words()
        #expected = 'forty-two'
        #self.assertEqual(result,expected)
        pass

#def load_tests(loader, tests, ignore):
#    tests.addTests(doctest.DocTestSuite(example))
#    return tests

if __name__ == '__main__':
    unittest.main()
