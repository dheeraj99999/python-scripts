Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #for finding square root
>>> x=sqrt(25)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x=sqrt(25)
NameError: name 'sqrt' is not defined
>>> import math
>>> x=math.sqrt(25)
>>> x
5.0
>>> x=math.sqrt(15)
>>> x
3.872983346207417
>>> #to print float function values
>>> #to print floar function values
>>> print(math.floor(2.1))
2
>>> print(math.ceil(2.1))
3
>>> 3**2
9
>>> print(math.power(3,2))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(math.power(3,2))
AttributeError: module 'math' has no attribute 'power'
>>> print(math.pow(3,2))
9.0
>>>  print(math.pi)
 
SyntaxError: unexpected indent
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> import math as m
>>> m.sqrt(25)
5.0
>>> import sqrt as sq
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    import sqrt as sq
ModuleNotFoundError: No module named 'sqrt'
>>> 
================================ RESTART: Shell ================================
>>> math.sqrt(25)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    math.sqrt(25)
NameError: name 'math' is not defined
>>> from math import sqrt,pow
>>> pow(4,5)
1024.0
>>> sqrt(25)
5.0
>>> math
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    math
NameError: name 'math' is not defined
>>> help('math')
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> 
>>> (built-in)
SyntaxError: invalid syntax
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> 
>>> 2+5
7
>>> 