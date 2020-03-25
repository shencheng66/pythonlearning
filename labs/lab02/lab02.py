"""Lab 2: Functions """

## Coding

def a_or_c(grade):
    """
    We all know the saying "C's get degrees".
    We all would like to get an A, but sometimes
    a C will have to do. 

    Return whether the grade inputted
    would receive an A or C.

    >>> a_or_c(100)
    True
    >>> a_or_c(75)
    True
    >>> a_or_c(82)
    False
    >>> a_or_c(80)
    False
    >>> a_or_c(95)
    True
    >>> a_or_c(40)
    False
    """
    "*** YOUR CODE HERE ***"
    if grade > 90 or grade == 90:
        return True
    elif grade > 70 and grade < 80:
        return True
    elif grade == 70:
        return True
    else:
        return False


## Control

def min(x, y):
    """
    Return the minimum between x and y

    >>> min(1,2)
    1
    >>> min(3,1)
    1
    >>> min(2,3)
    2
    >>> min(0, 67777)
    0
    >>> min(-1, -5)
    -5
    >>> min(-7, -1)
    -7
    >>> min(0, 0)
    0
    """
    "*** YOUR CODE HERE ***"
    if x < y:
        return x
    elif x == y:
        return x
    elif x > y:
        return y


## Transformation

def abs_value_equal(x, y):
    """Return whether or not the absolute value of both numbers is the same.

    Please refrain from using libraries (abs)

    >>> abs_value_equal(-2, -2)
    True
    >>> abs_value_equal(-3, 3)
    True
    >>> abs_value_equal(1, 2)
    False
    >>> abs_value_equal(3, 3)
    True
    >>> abs_value_equal(-6, -6)
    True
    >>> abs_value_equal(-1, -5)
    False
    >>> abs_value_equal(5, -6)
    False
    """
    "*** YOUR CODE HERE ***"

    if x < 0 and y < 0:
        x,y = -x,-y
    elif x < 0 and y > 0:
        x,y = -x,y
    elif x > 0 and y < 0:
        x,y = x,-y
    if x == y:
        return True
    else:
        return False

## Representation

def mirror(num1, num2):
    """
    Return if num1 is num2 backwards

    >>> mirror(121, 121)
    True
    >>> mirror(543, 345)
    True
    >>> mirror(343, 436)
    False
    >>> mirror(33, 33)
    True
    >>> mirror(42, 52)
    False
    >>> mirror(12, 22)
    False
    """
    "*** YOUR CODE HERE ***"
    
    def find(n):
        i = 0
        while n > 10**i:
            i = i + 1
        return i

    a = find (num1)
    result = 0
    while num1 > 0:
        result = result + num1 % 10 * (10 **(a-1))
        num1 = num1 // 10
        a = a - 1
    
    if result == num2:
        return True
    else:
        return False

def add(a,b,c)
    return a+b+c

add(1,2,3)