# Question 1-3

def second_max(lst):
    """ 
    Return the second highest number in a list of positive integers.
    
    >>> second_max([3, 2, 1, 0])
    2
    >>> second_max([2, 3, 3, 4, 5, 6, 7, 2, 3])
    6
    >>> second_max([1, 5, 5, 5, 1])
    5
    >>> second_max([5, 6, 6, 7, 1])
    6
    >>> second_max([5, 6, 7, 7, 1])
    7
    """

    "*** YOUR CODE HERE ***"
    '''def max(lst):
        result = 0
        for i in lst:
            if i > result:
                result = i
        return result
    a = max(lst)
    lst.remove(a)
    result2  = 0 
    for j in lst:
        if j > result2 and j <= a:
            result2 = j
    return result2'''

    max = lst[0]
    second_max = lst[1]
    for i in lst[1:]:
        if i >= max:
            second_max = max
            max = i
    return second_max


from math import sqrt
def is_square(n):
    return float(sqrt(n)) == int(sqrt(n))

def squares(seq):
    """Returns a new list containing elements of the original list that are
    perfect squares.

    >>> seq = [49, 8, 2, 1, 102]
    >>> squares(seq)
    [49, 1]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    '''result = []
    for n in seq:
        if is_square(n) == True:
            result.append(n)
    return result'''

    return [x for x in seq if is_square(x)]
    
    


def pairs(n):
    """Returns a new list containing two element lists from values 1 to n
    >>> pairs(1)
    [[1, 1]]
    >>> x = pairs(2)
    >>> x
    [[1, 1], [2, 2]]
    >>> pairs(5)
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    >>> pairs(-1)
    []
    """
    "*** YOUR CODE HERE ***"
    result = []
    while n > 0:
        result = [[n,n]] + result
        n = n - 1
    return result

# Question 4

def where_above(lst, limit):
    """
    where_above behaves like table.where(column, are.above(limit)).
    The analogy is completed if you think of a column of a table as a list and return the filtered column instead of the entire table.

    >>> where_above([1, 2, 3], 2)
    [3]
    >>> where_above(range(13), 10)
    [11, 12]
    >>> where_above(range(123), 120)
    [121, 122]

    """
    "*** YOUR CODE HERE ***"
    result = []
    for x in lst:
        if x > limit:
            result = result + [x]
    return result


# Question 5

def minmax(s):
    """Return the minimum and maximum elements of a non-empty list. Hint: start 
    with defining two variables at the beginning. Do not use the built in 
    max or min functions

    >>> minmax([1, 2, -3])
    [-3, 2]
    >>> x = minmax([2])
    >>> x
    [2, 2]
    >>> minmax([4, 5, 4, 5, 1, 9, 0, 7])
    [0, 9]
    >>> minmax([100, -10, 1, 0, 10, -100])
    [-100, 100]
    """
    "*** YOUR CODE HERE ***"
    '''def max(s):
        result = s[0]
        for i in s:
            if i > result:
                result = i
        return result
    a = max(s)
    def min(s):
        result = s[0]
        for j in s:
            if j < result:
                result = j
        return result
    b = min(s)
    return [b,a]'''

    max = s[0]
    min = s[0]
    for i in s:
        if i > max:
            max = i
        if i < min:
            min = i
    return [min,max]


# Question 6s

def closest_power_2(x):
    """ Returns the closest power of 2 that is less than x
    >>> closest_power_2(6)
    4
    >>> closest_power_2(32)
    16
    >>> closest_power_2(87)
    64
    >>> closest_power_2(4095)
    2048
    >>> closest_power_2(524290)
    524288
    """
    "*** YOUR CODE HERE ***"
    n = 0 
    while 2**n < x:
        n = n + 1
    return 2**(n-1)

