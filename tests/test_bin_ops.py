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
from numbers import Number

import pytest

from polynomial import Polynomial


@pytest.mark.parametrize("lhs", [Polynomial(), Polynomial(2, -1),
                                 Polynomial(1, 7, 0, 4)])
def test_add_zero_polynomial(lhs: Polynomial) -> None:
    assert lhs + Polynomial() == lhs
    assert lhs == Polynomial() + lhs


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
def test_add_number(lhs: Polynomial, rhs: Number, sum: Polynomial) \
        -> None:
    assert lhs + rhs == sum
    assert rhs + lhs == sum


@pytest.mark.parametrize("lhs", [Polynomial(), Polynomial(2, -1),
                                 Polynomial(1, 7, 0, 4)])
def test_sub_zero_polynomial(lhs: Polynomial) -> None:
    assert lhs - Polynomial() == lhs
    assert lhs == lhs - Polynomial()
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
def test_sub_number(lhs: Polynomial, rhs: Number, diff: Polynomial) \
        -> None:
    assert lhs - rhs == diff
    assert rhs - lhs == -diff
