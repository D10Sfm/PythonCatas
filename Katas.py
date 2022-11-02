"""
1.
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
"""

from math import sqrt,isqrt

def find_next_square(sq):
    if not isqrt(sq) == sqrt(sq):
        return -1
    else:
        return int((sqrt(sq)+1)**2)





"""
2.
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""

def find_row(x):
    first = x*(x-1)+1
    return first
def row_sum_odd_numbers(n):
    start = find_row(n)
    return_num = 0
    for _ in range(n):
        return_num += start
        start += 2
    return return_num





"""
3.
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

def find_it(seq):
    if len(seq) % 2 != 0:
        uniq = set(i for i in seq)  # generate set from given sequence.
        for num in uniq:   # looping through the set.
            appearance = seq.count(num)   # counting the repeat of the num in the sequence.
            if appearance % 2 != 0:    # if apparition is odd so return the num
                return num
            else:
                continue
    else:
        return






"""
4.
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if not i.isdigit():
                return False
        return True
    else:
        return False




"""
5.
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable):
    new_ls = []
    for index,elem in enumerate(iterable):
        try:
            if elem == iterable[index+1]:
                continue
            else:
                new_ls.append(elem)
        except IndexError:
            new_ls.append(elem)
            break
    return new_ls