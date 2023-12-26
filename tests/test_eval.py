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


@pytest.mark.parametrize(("f", "x", "fx"), [(Polynomial(), 27.4, 0.0),
                                            (Polynomial(-1., 17.3, 0.0, 3.7),
                                             4.24, 238.487456),
                                            (Polynomial(2.5, 0.0, 0.0, 0.0,
                                                        -5.2, -0.4),
                                             -0.5, 2.121875)])
def test_eval_float_coeffs(f: Polynomial, x: Complex, fx: Complex) -> None:
    assert f(x) == fx
