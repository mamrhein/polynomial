# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright:   (c) 2023 ff. Michael Amrhein (michael@adrhinum.de)
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source$
# $Revision$


"""Univariate polynomials with rational coefficients."""

__all__ = ['Polynomial']

from fractions import Fraction
from itertools import dropwhile, chain, repeat, product
from numbers import Rational
from operator import add, sub
from typing import Union

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Polynomial:
    """
    Represents univariate polynomials with rational coefficients.

    In order to create an instance of `Polynomial`, call the class and provide
    a list of Rational numbers corresponding to the coefficients of the
    polynomial (in descending order: aₙ, aₙ₋₁, … a₁, a₀). Calling the class
    without any parameters will create a "zero polynomial".

    Examples
    ========
    >>> from polynomial import Polynomial
    >>> from fractions import Fraction
    >>> z = Polynomial()
    >>> z
    Polynomial()
    >>> f = Polynomial(1, -7, 0, 4)
    >>> repr(f)
    'Polynomial(1, -7, 0, 4)'
    >>> print(f)
    f(x) = x³ - 7⋅x² + 4
    >>> g = Polynomial(Fraction(1, 2), 0, 0, 0, Fraction(1, 4), 3)
    >>> str(g)
    'f(x) = ¹/₂⋅x⁵ + ¹/₄⋅x + 3'
    """
    __slots__ = '_coeffs'

    def __init__(self, *args: Rational) -> None:
        """
        Initialize new `Polynomial` instance.

        Args:
            *args: list of Rational coefficients

        Raises:
            TypeError: If any of the arguments is not a Rational instance.
            ValueError: If the first argument is equal to zero.
        """
        # Assign to slot first and check later in order to avoid exception
        # in call of __repr__ in error reporting.
        self._coeffs = tuple(args)
        if any(not isinstance(n, Rational) for n in args):
            raise TypeError("All coefficients must be rational numbers.")
        if len(args) > 0 and args[0] == 0:
            raise ValueError("First coeff must not be zero!")

    def degree(self) -> int:
        """
        Returns:
            The degree of the polynomial.
        """
        return len(self._coeffs) - 1

    def __eq__(self, other: Self) -> bool:
        """
        `self` == `other`

        Two polynomials are considered equal if their coefficients are equal.
        """
        return self._coeffs == other._coeffs

    def __gt__(self, other: Self) -> bool:
        """
        `self` > `other`

        A polynomials is considered greater than another if its degree is
        greater than the others degree or - in case the degrees are equal - if
        its coefficients are greater than the others coefficients.
        """
        if len(self._coeffs) == len(other._coeffs):
            return self._coeffs > other._coeffs
        return len(self._coeffs) > len(other._coeffs)

    def __ge__(self, other: Self) -> bool:
        """`self` >= `other`"""
        if len(self._coeffs) == len(other._coeffs):
            return self._coeffs >= other._coeffs
        return len(self._coeffs) > len(other._coeffs)

    def __hash__(self) -> int:
        """hash(self)"""
        return hash(self._coeffs)

    def __copy__(self) -> Self:
        """copy(self)"""
        return self

    def __deepcopy__(self) -> Self:
        """deepcopy(self)"""
        return self.__copy__()

    def eval(self, x: Rational) -> Rational:
        """
        Evaluates the polynomial at value `x`.

        Args:
            x: The value to evaluate the polynomial at

        Returns:
            f(x): The value of the polynomial at `x`
        """
        fx = 0
        for coeff in self._coeffs[:-1]:
            fx = (fx + coeff) * x
        return fx + self._coeffs[-1] if self._coeffs else 0

    __call__ = eval

    def __repr__(self) -> str:
        """repr(self)"""
        return "%s(%s)" % (self.__class__.__name__,
                           ", ".join(repr(c) for c in self._coeffs))

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
            return f"{s}{_to_str(c)}"
        if c == 1:
            x = "x"
        else:
            x = f"{_to_str(c)}⋅x"
        if e == 1:
            return f"{s}{x}"
        else:
            return f"{s}{x}{str(e).translate(_to_superscript)}"

    def __str__(self) -> str:
        """str(self)"""
        n = len(self._coeffs)
        if n == 0:
            return "f(x) = 0"
        s = "f(x) = "
        for i in range(n):
            s += self._term(i)
        return s

    def __neg__(self) -> Self:
        """-self"""
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

    def __add__(self, other: Union[Self, Rational]) -> Self:
        """self + other"""
        if isinstance(other, Polynomial):
            return self._add_sub(other, add)
        if isinstance(other, Rational):
            if len(self._coeffs) == 0:
                return Polynomial(other)
            return Polynomial(*self._coeffs[:-1], self._coeffs[-1] + other)
        raise TypeError(f"Can't add {type(other)}")

    __radd__ = __add__

    def __sub__(self, other: Union[Self, Rational]) -> Self:
        """self - other"""
        if isinstance(other, Polynomial):
            return self._add_sub(other, sub)
        if isinstance(other, Rational):
            if len(self._coeffs) == 0:
                return Polynomial(-other)
            return Polynomial(*self._coeffs[:-1], self._coeffs[-1] - other)
        raise TypeError(f"Can't sub {type(other)}")

    def __rsub__(self, other: Union[Self, Rational]) -> Self:
        """other - self"""
        return -self + other

    def __mul__(self, other: Union[Self, Rational]) -> Self:
        """self * other"""
        if isinstance(other, Polynomial):
            coeffs = list(
                repeat(0, len(self._coeffs) + len(other._coeffs) - 1))
            it = product(enumerate(self._coeffs), enumerate(other._coeffs))
            for ((lhs_idx, lhs_val), (rhs_idx, rhs_val)) in it:
                coeffs[lhs_idx + rhs_idx] += lhs_val * rhs_val
            return Polynomial(*(dropwhile(lambda x: x == 0, coeffs)))
        if isinstance(other, Rational):
            if other == 0:
                return Polynomial()
            return Polynomial(*((c * other) for c in self._coeffs))

    __rmul__ = __mul__

    def __divmod__(self, other: Union[Self, Rational]) -> (Self, Self):
        """divmod(self, other)"""
        if isinstance(other, Polynomial):
            # Expanded synthetic division
            if other == Polynomial.ZERO:
                raise ZeroDivisionError("Cannot divide by zero.")
            d = other.degree()
            qr = list(self._coeffs)
            n = other._coeffs[0]
            for i in range(len(self._coeffs) - d):
                c = Fraction(qr[i] / n)
                if c.denominator == 1:
                    c = c.numerator
                qr[i] = c
                if c != 0:
                    for j in range(1, len(other._coeffs)):
                        qr[i + j] -= c * other._coeffs[j]
            return (Polynomial(*qr[:-d]),
                    Polynomial(*dropwhile(lambda a: a == 0, qr[-d:])))
        if isinstance(other, Rational):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return divmod(self, Polynomial(other))

    def __rdivmod__(self, other: Rational) -> (Self, Self):
        """divmod(other, self)"""
        return divmod(Polynomial(other), self)

    def __floordiv__(self, other: Union[Self, Rational]) -> Self:
        """self // other"""
        return divmod(self, other)[0]

    def __rfloordiv__(self, other: Rational) -> Self:
        """other // self"""
        return divmod(other, self)[0]

    def __mod__(self, other: Union[Self, Rational]) -> Self:
        """self % other"""
        return divmod(self, other)[1]

    def __rmod__(self, other: Rational) -> Self:
        """other % self"""
        return divmod(other, self)[1]


Polynomial.ZERO = Polynomial()

# helper for conversion to str

_to_superscript = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
_to_subscript = str.maketrans("-0123456789", "₋₀₁₂₃₄₅₆₇₈₉")


def _to_str(num: Rational) -> str:
    if type(num) == int:
        return str(num)
    elif num.denominator == 1:
        return str(num.numerator)
    else:
        return f"{str(num.numerator).translate(_to_superscript)}/" \
               f"{str(num.denominator).translate(_to_subscript)}"
