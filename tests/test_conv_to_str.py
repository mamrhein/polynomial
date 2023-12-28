# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright:   (c) 2023 ff. Michael Amrhein (michael@adrhinum.de)
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source$
# $Revision$


"""Test conversions to strings."""
from fractions import Fraction

import pytest

from polynomial import Polynomial


@pytest.mark.parametrize(("p", "s"), [(Polynomial.ZERO, "Polynomial()"),
                                      (Polynomial(2, -1), "Polynomial(2, -1)"),
                                      (Polynomial(-6), "Polynomial(-6)"),
                                      (Polynomial(-1, 7, 0, 4),
                                       "Polynomial(-1, 7, 0, 4)")])
def test_repr_int_coeffs(p: Polynomial, s: str) -> None:
    assert repr(p) == s


@pytest.mark.parametrize(("p", "s"), [
    (Polynomial(Fraction(2), -Fraction(1, 2)),
     "Polynomial(Fraction(2, 1), Fraction(-1, 2))"),
    (Polynomial(-1, Fraction(7, 4), 0, Fraction(4, 1)),
     "Polynomial(-1, Fraction(7, 4), 0, Fraction(4, 1))")])
def test_repr_rational_coeffs(p: Polynomial, s: str) -> None:
    assert repr(p) == s


@pytest.mark.parametrize(("p", "s"), [(Polynomial(), "f(x) = 0"),
                                      (Polynomial(-238), "f(x) = -238"),
                                      (Polynomial(7, -3), "f(x) = 7x - 3"),
                                      (Polynomial(1, 7, 0, 4),
                                       "f(x) = x^3 + 7x^2 + 4"),
                                      (Polynomial(5, 0, 0, -1, -1, 19),
                                       "f(x) = 5x^5 - x^2 - x + 19")])
def test_str_int_coeffs(p: Polynomial, s: str) -> None:
    assert str(p) == s


@pytest.mark.parametrize(("p", "s"),
                         [(Polynomial(Fraction(-23, 8)), "f(x) = -23/8"),
                          (Polynomial(Fraction(7, 2), -3), "f(x) = 7/2x - 3"),
                          (Polynomial(Fraction(1, 10), Fraction(7, 4),
                                      Fraction(0, 2), Fraction(-1, 4)),
                           "f(x) = 1/10x^3 + 7/4x^2 - 1/4"),
                          (Polynomial(Fraction(5, 7), 0, 0, Fraction(-1),
                                      Fraction(-1, 3), 19),
                           "f(x) = 5/7x^5 - x^2 - 1/3x + 19")])
def test_str_rational_coeffs(p: Polynomial, s: str) -> None:
    assert str(p) == s
