# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright:   (c) 2023 ff. Michael Amrhein (michael@adrhinum.de)
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source$
# $Revision$


"""Test Polymial constructor."""

import pytest

from polynomial import Polynomial


def test_leading_arg_zero() -> None:
    with pytest.raises(ValueError):
        Polynomial(0, 3)


def test_non_number_in_args() -> None:
    with pytest.raises(TypeError):
        Polynomial(1, 3, 2., 4)
