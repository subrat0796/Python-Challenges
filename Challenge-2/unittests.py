import unittest

from jsonparser import is_valid_json

class TestIsValidJson(unittest.TestCase):
    def test_valid_json(self):

        self.assertTrue(is_valid_json('./tests/step1/valid.json'))
        self.assertTrue(is_valid_json('./tests/step2/valid.json'))
        self.assertTrue(is_valid_json('./tests/step3/valid.json'))
        self.assertTrue(is_valid_json('./tests/step4/valid.json'))

    def test_invalid_json(self):

        self.assertFalse(is_valid_json('./tests/step1/invalid.json'))
        self.assertFalse(is_valid_json('./tests/step2/invalid.json'))
        self.assertFalse(is_valid_json('./tests/step3/invalid.json'))
        self.assertFalse(is_valid_json('./tests/step4/invalid.json'))

    def test_nonexistent_json(self):

        self.assertFalse(is_valid_json('./tests/invalid.json'))

if __name__ == '__main__':
    unittest.main()