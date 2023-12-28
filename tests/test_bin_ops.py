# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright:   (c) 2023 ff. Michael Amrhein (michael@adrhinum.de)
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source$
# $Revision$


"""Test binary ops"""
from fractions import Fraction

import pytest

from polynomial import Polynomial


@pytest.mark.parametrize("lhs", [Polynomial(), Polynomial(2, -1),
                                 Polynomial(1, 7, 0, 4)])
def test_add_zero_polynomial(lhs: Polynomial) -> None:
    assert lhs + Polynomial() == lhs
    assert Polynomial() + lhs == lhs


@pytest.mark.parametrize(("lhs", "rhs", "sum"),
                         [(Polynomial(12),
                           Polynomial(2, -1),
                           Polynomial(2, 11)),
                          (Polynomial(1, 7, 0, 4),
                           Polynomial(-9, 2, 0),
                           Polynomial(1, -2, 2, 4)),
                          (Polynomial(1, 7, 0, 4),
                           Polynomial(-1, -7, 2, 0),
                           Polynomial(2, 4)),
                          ])
def test_add_polynomial(lhs: Polynomial, rhs: Polynomial, sum: Polynomial) \
        -> None:
    assert lhs + rhs == sum
    assert rhs + lhs == sum


@pytest.mark.parametrize(("lhs", "rhs", "sum"),
                         [(Polynomial(), 28, Polynomial(28)),
                          (Polynomial(12), -8, Polynomial(4)),
                          (Polynomial(1, 7, 0, 4),
                           3,
                           Polynomial(1, 7, 0, 7)),
                          (Polynomial(1, 7, 0, 4),
                           -4,
                           Polynomial(1, 7, 0, 0)),
                          ])
def test_add_int(lhs: Polynomial, rhs: int, sum: Polynomial) \
        -> None:
    assert lhs + rhs == sum
    assert rhs + lhs == sum


@pytest.mark.parametrize("lhs", [Polynomial(), Polynomial(2, -1),
                                 Polynomial(1, 7, 0, 4)])
def test_sub_zero_polynomial(lhs: Polynomial) -> None:
    assert lhs - Polynomial() == lhs
    assert Polynomial() - lhs == -lhs


@pytest.mark.parametrize(("lhs", "rhs", "diff"),
                         [(Polynomial(2, 2),
                           Polynomial(2, -1),
                           Polynomial(3)),
                          (Polynomial(1, -7, 0, 4),
                           Polynomial(-9, 2, 4),
                           Polynomial(1, 2, -2, 0)),
                          ])
def test_sub_polynomial(lhs: Polynomial, rhs: Polynomial, diff: Polynomial) \
        -> None:
    assert lhs - rhs == diff
    assert rhs - lhs == -diff


@pytest.mark.parametrize(("lhs", "rhs", "diff"),
                         [(Polynomial(), 28, Polynomial(-28)),
                          (Polynomial(12), -8, Polynomial(20)),
                          (Polynomial(1, 7, 0, 4),
                           3,
                           Polynomial(1, 7, 0, 1)),
                          (Polynomial(1, 7, 0, 4),
                           4,
                           Polynomial(1, 7, 0, 0)),
                          ])
def test_sub_number(lhs: Polynomial, rhs: int, diff: Polynomial) \
        -> None:
    assert lhs - rhs == diff
    assert rhs - lhs == -diff


@pytest.mark.parametrize("lhs", [Polynomial(), Polynomial(2, -1),
                                 Polynomial(1, 7, 0, 4)])
def test_mul_zero_polynomial(lhs: Polynomial) -> None:
    assert lhs * Polynomial() == Polynomial()
    assert Polynomial() * lhs == Polynomial()


@pytest.mark.parametrize(("lhs", "rhs", "prod"),
                         [(Polynomial(12),
                           Polynomial(2, -1),
                           Polynomial(24, -12)),
                          (Polynomial(1, 7, 0, 4),
                           Polynomial(-9, 2, 0),
                           Polynomial(-9, -61, 14, -36, 8, 0)),
                          (Polynomial(1, 7, 1, 4),
                           Polynomial(-1, -7, 2, 0),
                           Polynomial(-1, -14, -48, 3, -26, 8, 0)),
                          ])
def test_mul_polynomial(lhs: Polynomial, rhs: Polynomial, prod: Polynomial) \
        -> None:
    assert lhs * rhs == prod
    assert rhs * lhs == prod


@pytest.mark.parametrize(("lhs", "rhs", "prod"),
                         [(Polynomial(), 28, Polynomial()),
                          (Polynomial(12), -8, Polynomial(-96)),
                          (Polynomial(1, 7, 0, 4),
                           3,
                           Polynomial(3, 21, 0, 12)),
                          (Polynomial(1, 7, 0, 4),
                           -4,
                           Polynomial(-4, -28, 0, -16)),
                          ])
def test_mul_int(lhs: Polynomial, rhs: int, prod: Polynomial) \
        -> None:
    assert lhs * rhs == prod
    assert rhs * lhs == prod


@pytest.mark.parametrize("f", [Polynomial(2, -1),
                               Polynomial(1, 7, 0, 4)])
def test_divmod_zero_polynomial(f: Polynomial) -> None:
    assert divmod(Polynomial(), f) == (Polynomial(), Polynomial())
    with pytest.raises(ZeroDivisionError):
        divmod(f, Polynomial())


@pytest.mark.parametrize(("lhs", "rhs", "quot", "rem"),
                         [(Polynomial(12),
                           Polynomial(2, -1),
                           Polynomial(),
                           Polynomial(12),),
                          (Polynomial(-9, -61, 14, -36, 8, 0),
                           Polynomial(-9, 2, 0),
                           Polynomial(1, 7, 0, 4),
                           Polynomial(),),
                          (Polynomial(4, -1, 2, 1, 0, -1),
                           Polynomial(1, 0, 1),
                           Polynomial(4, -1, -2, 2),
                           Polynomial(2, -3),),
                          (Polynomial(6, -2, 0, -4, 0, 3, 3),
                           Polynomial(2, 0, 2, -3),
                           Polynomial(3, -1, -3, Fraction(7, 2)),
                           Polynomial(3, -13, Fraction(27, 2)),),
                          ])
def test_divmod_polynomial(lhs: Polynomial, rhs: Polynomial,
                           quot: Polynomial, rem: Polynomial) \
        -> None:
    assert lhs // rhs == quot
    assert lhs % rhs == rem
    assert lhs == quot * rhs + rem
