#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour.models.deprecated` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from colour.models.deprecated import (
    RGB_to_HSV,
    HSV_to_RGB,
    RGB_to_HSL,
    HSL_to_RGB,
    RGB_to_CMY,
    CMY_to_RGB,
    CMY_to_CMYK,
    CMYK_to_CMY)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestRGB_to_HSV',
           'TestHSV_to_RGB',
           'TestRGB_to_HSL',
           'TestHSL_to_RGB',
           'TestRGB_to_CMY',
           'TestCMY_to_RGB',
           'TestCMY_to_CMYK',
           'TestCMYK_to_CMY']


class TestRGB_to_HSV(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.RGB_to_HSV` definition unit tests
    methods.
    """

    def test_RGB_to_HSV(self):
        """
        Tests :func:`colour.models.deprecated.RGB_to_HSV` definition.
        """

        np.testing.assert_almost_equal(
            RGB_to_HSV(np.array([0.25, 0.60, 0.05])),
            np.array([0.27272727, 0.91666667, 0.6]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_HSV(np.array([0, 0, 0])),
            np.array([0., 0., 0.]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_HSV(np.array([1, 1, 1])),
            np.array([0., 0., 1.]),
            decimal=7)

    def test_n_dimensions_RGB_to_HSV(self):
        """
        Tests :func:`colour.models.deprecated.RGB_to_HSV` definition
        n-dimensions support.
        """

        RGB = np.array([0.25, 0.60, 0.05])
        HSV = np.array([0.27272727, 0.91666667, 0.6])
        np.testing.assert_almost_equal(
            RGB_to_HSV(RGB),
            HSV,
            decimal=7)

        RGB = np.tile(RGB, (6, 1))
        HSV = np.tile(HSV, (6, 1))
        np.testing.assert_almost_equal(
            RGB_to_HSV(RGB),
            HSV,
            decimal=7)

        RGB = np.reshape(RGB, (2, 3, 3))
        HSV = np.reshape(HSV, (2, 3, 3))
        np.testing.assert_almost_equal(
            RGB_to_HSV(RGB),
            HSV,
            decimal=7)


class TestHSV_to_RGB(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.HSV_to_RGB` definition unit tests
    methods.
    """

    def test_HSV_to_RGB(self):
        """
        Tests :func:`colour.models.deprecated.HSV_to_RGB` definition.
        """

        np.testing.assert_almost_equal(
            HSV_to_RGB(np.array([0.27272727, 0.91666667, 0.6])),
            np.array([0.25, 0.60, 0.05]),
            decimal=7)

        np.testing.assert_almost_equal(
            HSV_to_RGB(np.array([0, 0, 0])),
            np.array([0., 0., 0.]),
            decimal=7)

        np.testing.assert_almost_equal(
            HSV_to_RGB(np.array([0, 0, 1])),
            np.array([1., 1., 1.]),
            decimal=7)

    def test_n_dimensions_HSV_to_RGB(self):
        """
        Tests :func:`colour.models.deprecated.HSV_to_RGB` definition
        n-dimensions support.
        """

        HSV = np.array([0.27272727, 0.91666667, 0.6])
        RGB = np.array([0.25, 0.60, 0.05])
        np.testing.assert_almost_equal(
            HSV_to_RGB(HSV),
            RGB,
            decimal=7)

        HSV = np.tile(HSV, (6, 1))
        RGB = np.tile(RGB, (6, 1))
        np.testing.assert_almost_equal(
            HSV_to_RGB(HSV),
            RGB,
            decimal=7)

        HSV = np.reshape(HSV, (2, 3, 3))
        RGB = np.reshape(RGB, (2, 3, 3))
        np.testing.assert_almost_equal(
            HSV_to_RGB(HSV),
            RGB,
            decimal=7)


class TestRGB_to_HSL(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.RGB_to_HSL` definition unit tests
    methods.
    """

    def test_RGB_to_HSL(self):
        """
        Tests :func:`colour.models.deprecated.RGB_to_HSL` definition.
        """

        np.testing.assert_almost_equal(
            RGB_to_HSL(np.array([0.25, 0.60, 0.05])),
            np.array([0.27272727, 0.84615385, 0.325]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_HSL(np.array([0, 0, 0])),
            np.array([0., 0., 0.]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_HSL(np.array([1, 1, 1])),
            np.array([0., 0., 1.]),
            decimal=7)

    def test_n_dimensions_RGB_to_HSL(self):
        """
        Tests :func:`colour.models.deprecated.RGB_to_HSL` definition
        n-dimensions support.
        """

        RGB = np.array([0.25, 0.60, 0.05])
        HSL = np.array([0.27272727, 0.84615385, 0.325])
        np.testing.assert_almost_equal(
            RGB_to_HSL(RGB),
            HSL,
            decimal=7)

        RGB = np.tile(RGB, (6, 1))
        HSL = np.tile(HSL, (6, 1))
        np.testing.assert_almost_equal(
            RGB_to_HSL(RGB),
            HSL,
            decimal=7)

        RGB = np.reshape(RGB, (2, 3, 3))
        HSL = np.reshape(HSL, (2, 3, 3))
        np.testing.assert_almost_equal(
            RGB_to_HSL(RGB),
            HSL,
            decimal=7)


class TestHSL_to_RGB(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.HSL_to_RGB` definition unit tests
    methods.
    """

    def test_HSL_to_RGB(self):
        """
        Tests :func:`colour.models.deprecated.HSL_to_RGB` definition.
        """

        np.testing.assert_almost_equal(
            HSL_to_RGB(np.array([0.27272727, 0.84615385, 0.325])),
            np.array([0.25, 0.60, 0.05]),
            decimal=7)

        np.testing.assert_almost_equal(
            HSL_to_RGB(np.array([0, 0, 0])),
            np.array([0., 0., 0.]),
            decimal=7)

        np.testing.assert_almost_equal(
            HSL_to_RGB(np.array([0, 0, 1])),
            np.array([1., 1., 1.]),
            decimal=7)

    def test_n_dimensions_HSL_to_RGB(self):
        """
        Tests :func:`colour.models.deprecated.HSL_to_RGB` definition
        n-dimensions support.
        """

        HSL = np.array([0.27272727, 0.84615385, 0.325])
        RGB = np.array([0.25, 0.60, 0.05])
        np.testing.assert_almost_equal(
            HSL_to_RGB(HSL),
            RGB,
            decimal=7)

        HSL = np.tile(HSL, (6, 1))
        RGB = np.tile(RGB, (6, 1))
        np.testing.assert_almost_equal(
            HSL_to_RGB(HSL),
            RGB,
            decimal=7)

        HSL = np.reshape(HSL, (2, 3, 3))
        RGB = np.reshape(RGB, (2, 3, 3))
        np.testing.assert_almost_equal(
            HSL_to_RGB(HSL),
            RGB,
            decimal=7)


class TestRGB_to_CMY(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.RGB_to_CMY` definition unit tests
    methods.
    """

    def test_RGB_to_CMY(self):
        """
        Tests :func:`colour.models.deprecated.RGB_to_CMY` definition.
        """

        np.testing.assert_almost_equal(
            RGB_to_CMY(np.array([0.25, 0.60, 0.05])),
            np.array([0.75, 0.40, 0.95]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_CMY(np.array([0, 0, 0])),
            np.array([1., 1., 1.]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_CMY(np.array([1, 1, 1])),
            np.array([0., 0., 0.]),
            decimal=7)

    def test_n_dimensions_RGB_to_CMY(self):
        """
        Tests :func:`colour.models.deprecated.RGB_to_CMY` definition
        n-dimensions support.
        """

        RGB = np.array([0.25, 0.60, 0.05])
        CMY = np.array([0.75, 0.40, 0.95])
        np.testing.assert_almost_equal(
            RGB_to_CMY(RGB),
            CMY,
            decimal=7)

        RGB = np.tile(RGB, (6, 1))
        CMY = np.tile(CMY, (6, 1))
        np.testing.assert_almost_equal(
            RGB_to_CMY(RGB),
            CMY,
            decimal=7)

        RGB = np.reshape(RGB, (2, 3, 3))
        CMY = np.reshape(CMY, (2, 3, 3))
        np.testing.assert_almost_equal(
            RGB_to_CMY(RGB),
            CMY,
            decimal=7)


class TestCMY_to_RGB(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.CMY_to_RGB` definition unit tests
    methods.
    """

    def test_CMY_to_RGB(self):
        """
        Tests :func:`colour.models.deprecated.CMY_to_RGB` definition.
        """

        np.testing.assert_almost_equal(
            CMY_to_RGB(np.array([0.75, 0.40, 0.95])),
            np.array([0.25, 0.60, 0.05]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMY_to_RGB(np.array([1, 1, 1])),
            np.array([0., 0., 0.]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMY_to_RGB(np.array([0, 0, 0])),
            np.array([1., 1., 1.]),
            decimal=7)

    def test_n_dimensions_CMY_to_RGB(self):
        """
        Tests :func:`colour.models.deprecated.CMY_to_RGB` definition
        n-dimensions support.
        """

        CMY = np.array([0.75, 0.40, 0.95])
        RGB = np.array([0.25, 0.60, 0.05])
        np.testing.assert_almost_equal(
            CMY_to_RGB(CMY),
            RGB,
            decimal=7)

        CMY = np.tile(CMY, (6, 1))
        RGB = np.tile(RGB, (6, 1))
        np.testing.assert_almost_equal(
            CMY_to_RGB(CMY),
            RGB,
            decimal=7)

        CMY = np.reshape(CMY, (2, 3, 3))
        RGB = np.reshape(RGB, (2, 3, 3))
        np.testing.assert_almost_equal(
            CMY_to_RGB(CMY),
            RGB,
            decimal=7)


class TestCMY_to_CMYK(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.CMY_to_CMYK` definition unit tests
    methods.
    """

    def test_CMY_to_CMYK(self):
        """
        Tests :func:`colour.models.deprecated.CMY_to_CMYK` definition.
        """

        np.testing.assert_almost_equal(
            CMY_to_CMYK(np.array([0.75, 0.40, 0.95])),
            np.array([0.58333333, 0., 0.91666667, 0.4]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMY_to_CMYK(np.array([0.15, 1, 1])),
            np.array([0., 1., 1., 0.15]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMY_to_CMYK(np.array([0.15, 0, 0])),
            np.array([0.15, 0., 0., 0.]),
            decimal=7)

    def test_n_dimensions_CMY_to_CMYK(self):
        """
        Tests :func:`colour.models.deprecated.CMY_to_CMYK` definition
        n-dimensions support.
        """

        CMY = np.array([0.75, 0.40, 0.95])
        CMYK = np.array([0.58333333, 0., 0.91666667, 0.4])
        np.testing.assert_almost_equal(
            CMY_to_CMYK(CMY),
            CMYK,
            decimal=7)

        CMY = np.tile(CMY, (6, 1))
        CMYK = np.tile(CMYK, (6, 1))
        np.testing.assert_almost_equal(
            CMY_to_CMYK(CMY),
            CMYK,
            decimal=7)

        CMY = np.reshape(CMY, (2, 3, 3))
        CMYK = np.reshape(CMYK, (2, 3, 4))
        np.testing.assert_almost_equal(
            CMY_to_CMYK(CMY),
            CMYK,
            decimal=7)


class TestCMYK_to_CMY(unittest.TestCase):
    """
    Defines :func:`colour.models.deprecated.CMYK_to_CMY` definition unit tests
    methods.
    """

    def test_CMYK_to_CMY(self):
        """
        Tests :func:`colour.models.deprecated.CMYK_to_CMY` definition.
        """

        np.testing.assert_almost_equal(
            CMYK_to_CMY(np.array([0.58333333, 0, 0.91666667, 0.4])),
            np.array([0.75, 0.40, 0.95]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMYK_to_CMY(np.array([0, 1, 1, 0.15])),
            np.array([0.15, 1., 1.]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMYK_to_CMY(np.array([0.15, 0, 0, 0])),
            np.array([0.15, 0., 0.]),
            decimal=7)

    def test_n_dimensions_CMYK_to_CMY(self):
        """
        Tests :func:`colour.models.deprecated.CMYK_to_CMY` definition
        n-dimensions support.
        """

        CMYK = np.array([0.58333333, 0, 0.91666667, 0.4])
        CMY = np.array([0.75, 0.40, 0.95])
        np.testing.assert_almost_equal(
            CMYK_to_CMY(CMYK),
            CMY,
            decimal=7)

        CMYK = np.tile(CMYK, (6, 1))
        CMY = np.tile(CMY, (6, 1))
        np.testing.assert_almost_equal(
            CMYK_to_CMY(CMYK),
            CMY,
            decimal=7)

        CMYK = np.reshape(CMYK, (2, 3, 4))
        CMY = np.reshape(CMY, (2, 3, 3))
        np.testing.assert_almost_equal(
            CMYK_to_CMY(CMYK),
            CMY,
            decimal=7)


if __name__ == '__main__':
    unittest.main()
