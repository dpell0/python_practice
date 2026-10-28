"""
Given a list of integers, return the number that appears most often.
"""
#solution 1
def mostFrequent(numbers):
    track = {}

    for i in numbers:
        if i in track:
            track[i] += 1
        else:
            track[i] = 1

    answer = numbers[0]

    for i in track:
        if track[i] > track[answer]:
            answer = i

    return answer


#test cases
print("expected: 3 OUTPUT '", mostFrequent([3, 1, 3, 2, 3, 2]), "'")
print("expected: 4 OUTPUT '", mostFrequent([4, 2, 2, 4]), "'")
print("expected: 2 OUTPUT '", mostFrequent([2, 4, 4, 2]), "'")
print("expected: 7 OUTPUT '", mostFrequent([7, 8, 9]), "'")
print("expected: -1 OUTPUT '", mostFrequent([-1, -1, 2]), "'")
print("expected: 0 OUTPUT '", mostFrequent([0, 1, 0]), "'")
print("expected: 5 OUTPUT '", mostFrequent([5]), "'")