# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_macadam_limits.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`colour.optimal.macadam_limits` module.

**Others:**

"""

from __future__ import unicode_literals

import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from colour.optimal import is_within_macadam_limits

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["TestIsWithinMacadamLimits"]


class TestIsWithinMacadamLimits(unittest.TestCase):
    """
    Defines :func:`colour.optimal.macadam_limits.is_within_macadam_limits`
    definition units tests methods.
    """

    def test_is_within_macadam_limits(self):
        """
        Tests :func:`colour.optimal.macadam_limits.is_within_macadam_limits`
        definition.
        """

        self.assertTrue(
            is_within_macadam_limits((0.3205, 0.4131, 0.51), "A"))
        self.assertFalse(
            is_within_macadam_limits((0.0005, 0.0031, 0.001), "A"))
        self.assertTrue(
            is_within_macadam_limits((0.4325, 0.3788, 0.1034), "C"))
        self.assertFalse(
            is_within_macadam_limits((0.0025, 0.0088, 0.034), "C"))


if __name__ == "__main__":
    unittest.main()
