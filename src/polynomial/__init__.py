# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright:   (c) 2023 ff. Michael Amrhein (michael@adrhinum.de)
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source$
# $Revision$


"""Polynomials"""
from itertools import dropwhile, chain, repeat
from numbers import Number
from operator import add, sub
from typing import Self, Union


class Polynomial:
    """
    Represents a polynomial.
    """
    __slots__ = '_coeffs'

    def __init__(self, *args: int) -> None:
        assert all(isinstance(n, Number) for n in args), \
            "All coefficients must be numbers."
        assert len(args) == 0 or args[0] != 0, "First coeff must not be zero!"
        self._coeffs = tuple(args)

    def degree(self) -> int:
        """
        Returns:
            The degree of the polynomial.
        """
        return len(self._coeffs) - 1

    def __eq__(self, other: Self) -> bool:
        """
        Compares two polynomials.

        Args:
            other: Some other polynomial

        Returns:
            true if both polynomials are equal, false otherwise
        """
        return self._coeffs == other._coeffs

    def __hash__(self) -> int:
        return hash(self._coeffs)

    def __copy__(self) -> Self:
        return self

    def __deepcopy__(self) -> Self:
        return self.__copy__()

    def __repr__(self) -> str:
        return "%s(%s)" % (self.__class__.__name__,
                           ", ".join(str(c) for c in self._coeffs))

    def _term(self, i: int) -> str:
        c = self._coeffs[i]
        if c == 0:
            return ""
        if i == 0:
            s = '' if c > 0 else '-'
        else:
            s = " + " if c > 0 else " - "
        c = abs(c)
        e = self.degree() - i
        if e == 0:
            return f"{s}{c}"
        if c == 1:
            x = "x"
        else:
            x = f"{c}x"
        if e == 1:
            return f"{s}{x}"
        else:
            return f"{s}{x}^{e}"

    def __str__(self) -> str:
        n = len(self._coeffs)
        if n == 0:
            return "f(x) = 0"
        s = "f(x) = "
        for i in range(n):
            s += self._term(i)
        return s

    def __neg__(self) -> Self:
        res = Polynomial()
        res._coeffs = tuple(-a for a in self._coeffs)
        return res

    def _add_sub(self, other: Self, op) -> Self:
        lhs_n = len(self._coeffs)
        rhs_n = len(other._coeffs)
        m = max(lhs_n, rhs_n)
        lhs_it = chain(repeat(0, m - lhs_n), self._coeffs)
        rhs_it = chain(repeat(0, m - rhs_n), other._coeffs)
        res = Polynomial()
        res._coeffs = tuple(dropwhile(lambda c: c == 0,
                                      (op(a, b) for a, b in
                                       zip(lhs_it, rhs_it))))
        return res

    def __add__(self, other: Union[Self, Number]):
        if isinstance(other, Polynomial):
            return self._add_sub(other, add)
        if isinstance(other, Number):
            if len(self._coeffs) == 0:
                return Polynomial(other)
            return Polynomial(*self._coeffs[:-1], self._coeffs[-1] + other)
        raise TypeError(f"Can't add {type(other)}")

    __radd__ = __add__

    def __sub__(self, other: Union[Self, Number]):
        if isinstance(other, Polynomial):
            return self._add_sub(other, sub)
        if isinstance(other, Number):
            if len(self._coeffs) == 0:
                return Polynomial(-other)
            return Polynomial(*self._coeffs[:-1], self._coeffs[-1] - other)
        raise TypeError(f"Can't sub {type(other)}")

    def __rsub__(self, other: Union[Self, Number]):
        return -self + other


Polynomial.ZERO = Polynomial()
