import string
from typing import Union, List

# constants
inverted_charnumber = dict(enumerate(string.ascii_lowercase, start=1))
CHAR_NUMBER = {value: key for key, value in inverted_charnumber.items()}


def lovesongs_solver(
        love_song: str,
        questions: List[List[int]]) -> list:
    """
    The first line contains two integers: n and q
        n -> Length of the Song. 1 <= n <= 100000
        q -> Number of questions. 1 <= q <= 100000

    The second line contains one string: s
        s -> the song, consisting of n lowercase letters of English letters

    The next lines contains two integers: l and r
        l and r -> the bounds of the question.  1 <= l <= r <= n

    Expected output:
        - Print q lines: for each question print the length of the string obtained.

    """
    cumsum_list = [0]
    counter = 0

    # iter through the song-str / get char_number / then calculate cumsum
    for char in love_song:
        counter += CHAR_NUMBER[char]
        cumsum_list.append(counter)

    # get the answer
    results = []
    for left, right in questions:
        results.append(cumsum_list[right] - cumsum_list[left - 1])

    return results



if __name__ == '__main__':
    love_song = 'abacaba'
    questions = [[1, 3], [2, 5], [1, 7]]
    asnwer = lovesongs_solver(love_song, questions)
    print(asnwer)
