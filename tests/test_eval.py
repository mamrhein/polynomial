# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright:   (c) 2023 ff. Michael Amrhein (michael@adrhinum.de)
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source$
# $Revision$


"""Test evaluation of polynomials."""
from fractions import Fraction
from numbers import Complex

import pytest

from polynomial import Polynomial


@pytest.mark.parametrize(("f", "x", "fx"), [(Polynomial(), 27, 0),
                                            (Polynomial(-1, 17, 0, 3),
                                             4, 211),
                                            (Polynomial(2, 0, 0, 0, -5, -9),
                                             -7, -33588)])
def test_eval_int_coeffs(f: Polynomial, x: Complex, fx: Complex) -> None:
    assert f.eval(x) == fx


@pytest.mark.parametrize(("f", "x", "fx"), [(Polynomial(), 274, 0.0),
                                            (
                                                    Polynomial(-1,
                                                               Fraction(173,
                                                                        2), 0,
                                                               Fraction(37,
                                                                        4)),
                                                    4, Fraction(5317, 4)),
                                            (Polynomial(Fraction(25, 2), 0, 0,
                                                        0, Fraction(-26, 5),
                                                        Fraction(-2, 5)),
                                             Fraction(-1, 2),
                                             Fraction(579, 320))])
def test_eval_rational_coeffs(f: Polynomial, x: Complex, fx: Complex) -> None:
    assert f(x) == fx
