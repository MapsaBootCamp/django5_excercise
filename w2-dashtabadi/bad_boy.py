from typing import Iterable

def badboy_solver(testcases: Iterable):
    for _testcase in testcases:
        m, n, i, j = map(int, _testcase.split())
        print(1, 1, m, n)


if __name__ == '__main__':
    testcases = (
        '2 3 1 1',
        '4 4 1 2',
        '3 5 2 2',
        '5 1 2 1',
        '3 1 3 1',
        '1 1 1 1',
        '1000000000 1000000000 1000000000 50',
    )

    answer = badboy_solver(
        testcases=testcases,
    )

