# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

######################
#### Linked Lists ####
######################

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"
    if lst == []:
        return Link.empty
    else:
        return Link(lst[0], list_to_link(lst[1:]))


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print_link(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        return link
    elif isinstance(link.first, Link):
        return Link(deep_map_mut(fn, link.first), deep_map_mut(fn, link.rest))
    else:
       return Link(fn(link.first), deep_map_mut(fn, link.rest))




def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"
    return reverse_helper(link, Link.empty)
    
    result = Link.empty
    a = link
    while a != Link.empty:
        result = Link(a.first, result)
        a = a.rest
    return result

def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    "*** YOUR CODE HERE ***"
    reverse_helper(link, Link.empty)

def reverse_helper(link, result):
    if link.rest == Link.empty:
        link.rest = result
    else:
        result = Link(link.first, result)
        reverse_helper(link.rest, result)


def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print_link(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print_link(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
    "*** YOUR CODE HERE ***"
    

    if index > len(link) - 1:
        raise IndexError
    if index != 0:
        link1 = Link(value, getlink(link, index))
        link2 = getlink(link, (index-1))
        link2.rest = link1
    else: 
        result = Link(link.first, link.rest)
        link.first = value
        link.rest = result
    
def getlink(link, index):
    a = 0
    while link != Link.empty:
        if a != index:
            a = a + 1
            link = link.rest
        else:
            return link





def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print_link(new)
    <1 4 1>
    """
    "*** YOUR CODE HERE ***"
    # result = getlink(link, start)
    # result2 = getlink(link, (end-1))
    # result2.rest = Link.empty
    # return result

    result = getlink(link, start)
    result2 = getlink(result, (end-start-1))
    result2.rest = Link.empty
    return result




## Optional Questions

def rotate(link, n):
    """Rotates the Link so that its elements are shifted to the right n times.

    >>> link = Link(1, Link(2, Link(3)))
    >>> link = rotate(link, 0)
    >>> link
    Link(1, Link(2, Link(3)))
    >>> link = rotate(link, 1)
    >>> link
    Link(3, Link(1, Link(2)))
    >>> link = rotate(link, 2)
    >>> link
    Link(1, Link(2, Link(3)))
    >>> rotate(link, 5)
    Link(2, Link(3, Link(1)))
    >>> link = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> rotate(link, 4)
    Link(3, Link(4, Link(5, Link(6, Link(1, Link(2))))))
    """
    "*** YOUR CODE HERE ***"



