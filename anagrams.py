"""
Given two strings, return True if they are anagrams and False otherwise.
"""
#solution 1 
def isAnagram(first, second):
    if len(first) != len(second):
        return False

    seenFirst = {}
    seenSecond = {}

    for i in range(len(first)):
        if first[i] in seenFirst:
            seenFirst[first[i]] += 1
        else:
            seenFirst[first[i]] = 1

        if second[i] in seenSecond:
            seenSecond[second[i]] += 1
        else:
            seenSecond[second[i]] = 1

    return seenFirst == seenSecond


#test cases
print("expected: True OUTPUT '", isAnagram("listen", "silent"), "'")
print("expected: False OUTPUT '", isAnagram("hello", "world"), "'")
print("expected: True OUTPUT '", isAnagram("aab", "aba"), "'")
print("expected: False OUTPUT '", isAnagram("aab", "abb"), "'")
print("expected: False OUTPUT '", isAnagram("ab", "abc"), "'")
print("expected: True OUTPUT '", isAnagram("", ""), "'")
print("expected: True OUTPUT '", isAnagram("aaa", "aaa"), "'")