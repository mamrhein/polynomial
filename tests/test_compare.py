# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright:   (c) 2023 ff. Michael Amrhein (michael@adrhinum.de)
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source$
# $Revision$


"""Test comparisions."""

import pytest

from polynomial import Polynomial


@pytest.mark.parametrize("lhs", [Polynomial(), Polynomial(2, -1),
                                 Polynomial(1, 7, 0, 4)])
@pytest.mark.parametrize("rhs", [Polynomial(), Polynomial(2, -1),
                                 Polynomial(1, 7, 0, 4)])
def test_equality(lhs: Polynomial, rhs: Polynomial) -> None:
    if lhs.degree() == rhs.degree():
        assert lhs == rhs
    else:
        assert lhs != rhs
