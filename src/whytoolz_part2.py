"""
WhyToolz Part II: Sequence Manipulation

Great work getting through Part One!

In this section, you'll implement functions that work with sequences
and iterables in various ways: slicing, dropping elements, combining
sequences, extracting data, and more.

These functions return CONCRETE LISTS OR VALUES, not generators.
This makes them easier to understand and debug while you learn the algorithms.

Focus on:
- Slicing and subsetting sequences
- Working with iterables (anything you can loop over)
- Combining and transforming sequences
- Building reusable sequence operations
- Extracting data from collections

See: https://toolz.readthedocs.io/en/latest/api.html#itertoolz
"""
from itertools import zip_longest

from collections import deque


def islice(seq, *args):
    """
    Slice a sequence and return a list of elements.

    Similar to itertools.islice, this function allows you to extract
    a subset of elements from a sequence.

    This is the foundation function for many of the sequence manipulation
    functions in Part II.

    Args:
        seq: Input sequence (can be any iterable)
        *args: Either:
            - Single argument (stop): islice(seq, 5) returns first 5 elements
            - Two arguments (start, stop): islice(seq, 2, 5) returns elements at indices 2, 3, 4
            - Three arguments (start, stop, step): islice(seq, 0, 10, 2) returns every 2nd element

    Returns:
        List of sliced elements from seq

    Example:
        >>> islice([1, 2, 3, 4, 5], 3)
        [1, 2, 3]
        >>> islice([1, 2, 3, 4, 5], 1, 4)
        [2, 3, 4]
        >>> islice([1, 2, 3, 4, 5], 0, 5, 2)
        [1, 3, 5]

    Hint: Parse the *args to determine start, stop, and step values,
          then iterate through the sequence collecting appropriate elements into a list.
    """
    lst = list(seq)
    if len(args) == 1:
        stop = args[0]
        return lst[:stop]
    if len(args) == 2:
        start, stop = args
        return lst[start:stop]
    if len(args) == 3:
        start, stop, step = args
        return lst[start:stop:step]


def drop(n, seq):
    """
    Skip the first n elements and return the rest as a list.

    Discards the first n elements and returns everything after.

    Args:
        n: Number of elements to skip
        seq: Input sequence

    Returns:
        List of all elements after the first n

    Example:
        >>> drop(2, [1, 2, 3, 4, 5])
        [3, 4, 5]
        >>> drop(3, 'hello')
        ['l', 'o']

    Hint: Use islice with a start parameter
    """

    lst = list(seq)
    for item in lst[:n]:
        lst.remove(item)
    return lst


def tail(n, seq):
    """
    Return the last n elements from a sequence.

    Note: Unlike take/drop, this returns a list (not a generator)
    because we need to see the whole sequence to know what the
    last n elements are.

    Args:
        n: Number of elements from the end
        seq: Input sequence

    Returns:
        List of the last n elements

    Example:
        >>> tail(2, [1, 2, 3, 4, 5])
        [4, 5]
        >>> tail(3, 'hello')
        ['l', 'l', 'o']

    Hint: Use collections.deque with maxlen, or convert to list and slice
    """
    lst = list(seq)
    if n == 0:
        return []
    return lst[-n:]



def concat(seqs):
    """
    Concatenate multiple sequences into a single list.

    Takes an iterable of iterables and returns all elements
    from all sequences in order.

    Args:
        seqs: An iterable of iterables

    Returns:
        List of all elements from all sequences

    Example:
        >>> concat([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
        >>> concat(['ab', 'cd', 'ef'])
        ['a', 'b', 'c', 'd', 'e', 'f']

    Hint: Nested loops to collect elements, or flatten the sequences
    """

    lst = list(seqs)
    sub_list = []
    flat_list = []
    for sub_list in lst:
        for item in sub_list:
            flat_list.append(item)
    return flat_list




def unique(seq):
    """
    Return unique elements from a sequence, preserving order.

    Only returns each distinct element once, in the order of first appearance.

    Args:
        seq: Input sequence (possibly with duplicates)

    Returns:
        List of unique elements in order of first appearance

    Example:
        >>> unique([1, 2, 3, 2, 1, 4])
        [1, 2, 3, 4]
        >>> unique('hello')
        ['h', 'e', 'l', 'o']

    Hint: Keep a set of seen elements, only collect if not seen before
    """
    lst = []
    for item in seq:
        if item not in lst:
            lst.append(item)
    return lst



def partition(n, seq):
    """
    Partition a sequence into tuples of length n.

    Splits the sequence into non-overlapping chunks of size n.
    If the sequence length isn't divisible by n, the last partition
    will be shorter.

    Args:
        n: Size of each partition
        seq: Input sequence

    Returns:
        List of tuples, each of size n (last may be shorter)

    Example:
        >>> partition(2, [1, 2, 3, 4, 5])
        [(1, 2), (3, 4), (5,)]
        >>> partition(3, 'hello')
        [('h', 'e', 'l'), ('l', 'o')]

    Hint: Use islice in a loop to grab n items at a time
    """
    lst = list(seq)
    count = 0
    part_list = []

    while count < len(lst):
        stop = count + n
        group = islice(lst, count, stop)
        part_list.append(tuple(group))

        count += n

    return part_list




def interleave(seqs):
    """
    Interleave multiple sequences element by element.

    Takes elements alternately from each sequence until all are exhausted.
    Shorter sequences are skipped once exhausted.

    Args:
        seqs: Multiple sequences to interleave

    Returns:
        List of interleaved elements

    Example:
        >>> interleave([[1, 2], [3, 4], [5, 6]])
        [1, 3, 5, 2, 4, 6]
        >>> interleave(['ab', 'cd'])
        ['a', 'c', 'b', 'd']

    Hint: Use zip_longest to handle sequences of different lengths
    """
    lst = list(seqs)
    interleaved_list = []
    max_len = 0
    for sublist in lst:
        if len(sublist) > max_len:
            max_len = len(sublist)

    for index in range(max_len):
        for sublist in lst:
            if index < len(sublist):
                interleaved_list.append(sublist[index])
    return interleaved_list




def pluck(key, seq):
    """
    Extract a specific key from a sequence of dictionaries.

    Returns the value of 'key' from each dictionary in seq.
    Useful for extracting a column from a list of records.

    Args:
        key: The key to extract from each dict
        seq: Sequence of dictionaries

    Returns:
        List of values corresponding to key from each dict

    Example:
        >>> people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> pluck('name', people)
        ['Alice', 'Bob']
        >>> pluck('age', people)
        [30, 25]

    Hint: Use a list comprehension to extract values
    """

    return [dic[key] for dic in seq]


def accumulate(func, seq, initial=None):
    """
    Return accumulated results of applying func to sequence elements.

    Like reduce(), but returns intermediate results at each step.
    This creates a list of running totals/accumulations.

    Args:
        func: Binary function to apply (takes two args, returns one)
        seq: Input sequence
        initial: Optional starting value

    Returns:
        List of accumulated values at each step

    Example:
        >>> accumulate(lambda x, y: x + y, [1, 2, 3, 4], 0)
        [0, 1, 3, 6, 10]
        >>> accumulate(lambda x, y: x * y, [1, 2, 3, 4], 1)
        [1, 1, 2, 6, 24]

    Hint: Keep a running accumulator, collect results at each step
    """
    acc_list = []

    if initial is None:
        flat_seq = seq
    else:
        flat_seq = [initial] + seq
    for i in flat_seq:
      if flat_seq.index(i) == 0:
       acc_list.append(i)
      else:
       acc_list.append(func(acc_list[-1], i))

    return acc_list


def sliding_window(n, seq):
    """
    Create a sliding window of size n over a sequence.

    Returns overlapping tuples of n consecutive elements.
    Each window slides one position from the previous.

    Args:
        n: Window size
        seq: Input sequence

    Returns:
        List of tuples, each containing n consecutive elements

    Example:
        >>> sliding_window(2, [1, 2, 3, 4])
        [(1, 2), (2, 3), (3, 4)]
        >>> sliding_window(3, 'hello')
        [('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]

    Hint: Use collections.deque with maxlen to maintain the window
    """
    slide_list = []
    if n > len(seq):
        return []

    for index in range(len(seq) - n + 1):
        small_lst = []
        for i in range(n):
            small_lst.append(seq[index+i])
        slide_list.append(tuple(small_lst)) # Changed to append tuple

    return slide_list



def take_nth(n, seq):
    """
    Return every nth element from a sequence.

    Takes elements at positions 0, n, 2n, 3n, ...

    Args:
        n: Take every nth element
        seq: Input sequence

    Returns:
        List of every nth element

    Example:
        >>> take_nth(2, [0, 1, 2, 3, 4, 5, 6])
        [0, 2, 4, 6]
        >>> take_nth(3, 'hello world')
        ['h', 'l', 'o', 'l']

    Hint: Use enumerate to track position, collect when position % n == 0
    """
    nth_list = []
    for index, elem in enumerate(seq):
        if index % n == 0:
            nth_list.append(elem)
    return nth_list
