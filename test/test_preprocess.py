import unittest
from unittest import TestCase

from pandemic import Preprocess

if __name__ == '__main__':
    unittest.main()


class TestPreprocess:
    def test_opener(self):
        pr = Preprocess()
        assert isinstance(pr.target, list)

    def test_drop_na_certain_col(self):
        assert False

    def test_prepare_trainset(self):
        assert False
