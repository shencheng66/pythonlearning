"""Homework 2."""

# Question 1

def harmonic_mean(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic_mean(2, 6)
    3.0
    >>> harmonic_mean(1, 1)
    1.0
    >>> harmonic_mean(2.5, 7.5)
    3.75
    >>> harmonic_mean(4, 12)
    6.0
    """
    "*** YOUR CODE HERE ***"
    return 2/((1/x)+(1/y))

# Question 2

def speed_converter(miles_per_min):
    """
    >>> speed_converter(0)
    0.0
    >>> speed_converter(0.5)
    1158.48
    >>> speed_converter(0.75)
    1737.72
    >>> speed_converter(2)
    4633.92
    """
    "*** YOUR CODE HERE ***"
    kilos_per_day = miles_per_min * 1.609 * 60 * 24
    return kilos_per_day


# Question 3

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"
    if a>c and b>c:
        return a*a + b*b
    elif a > b and c > b:
        return a*a + c*c
    elif b > a and c > a:
        return b*b + c*c
    else: 
        return a*a + b*b
# Question 4

def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    "*** YOUR CODE HERE ***"
    b = n - 1
    while b > 1:
        if (n*n-1)%b == 0:
            return b
        else:
            b = b - 1

# Question 5

from math import sin

def law_of_sines(a, b, c, A, B, C):
    """
    >>> law_of_sines(1, 1, 1, 1.0472, 1.0472, 1.0472)
    True
    >>> law_of_sines(1, 2, 3, 1, 2, 3)
    False
    """
    "*** YOUR CODE HERE ***"
    if sin(A)/a == sin(B)/b == sin(C)/c:
        return True
    else:
        return False


