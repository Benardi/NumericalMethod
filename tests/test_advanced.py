# -*- coding: utf-8 -*-

from .context import numerical_methods

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(numerical_methods.hmm())


if __name__ == '__main__':
    unittest.main()
