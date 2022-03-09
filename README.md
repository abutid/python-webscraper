# A small python script to help me learn python and get hands on experience on how to build applications with it.  


```python
def one_edit_away(s1, s2):
    # if difference between two words is more than 1 than its not one edit away
    if len(str(s1)) - len(str(s2)) > 1:
        return False

    edits = 0
    p1 = 0
    p2 = 0

    # continue until run out of words
    while p1 < len(s1) and p2 < len(s2):

        # non-matching character
        if s1[p1] != s2[p2]:

            # if first words longer - remove current character from string
            if len(s1) > len(s2):
                p1 += 1

            # if second words longer - remove current character from string
            elif len(s1) < len(s2):
                p2 += 1

            # length of both strings are the same
            else:
                p1 += 1
                p2 += 1

            edits += 1

        # current character both strings same
        else:
            p1 += 1
            p2 += 1

    # remove extra character from first string
    if p1 < len(s1):
        edits += 1

    return edits == 1


if __name__ == "__main__":
    print(one_edit_away("sad", "mad"))  # True
    print(one_edit_away("hello", "hell"))  # True
    print(one_edit_away("deed", "dead"))  # True
    print(one_edit_away("abcd", "abdbbg"))  # False

"""
Algorithm:

if the two strings are the same, there was no change
if the two strings are different, there are 3 outcomes

1. character was replaced
    - count how many positions have different character. if exactly 1 its a replaced if more than 1 than its different
    edit
2. character was removed
    - count number of positions with different character. when find difference, increment position of one of counters to
    skip over a character in one of strings
3. character was added

loop through each words to compare the character of the two strings

"""

```
