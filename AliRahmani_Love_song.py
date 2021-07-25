"""
n the first example Vasya is interested in three questions. In the first question Vasya considers
the substring "aba", that transforms to "abba", so the answer is equal to 4.
In the second question Vasya considers "baca", that transforms to "bbaccca", so the answer is 7.
In the third question Vasya considers the string "abacaba",that transforms to "abbacccabba" of length 11

"""
# alpha = 'abcdefghilmnopqrstyvwxyz'

alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z', ' '                        ]

vasya = 'vasya love'

# def love_song(vaysa,alphabet):
answer = ''
for i in vasya:
    if i == " ":
        answer += " "
        continue
    for j in range(0,len(alphabet)):
        if alphabet[j] == i:
            answer += str(i * (j+1))


print(alphabet)
print(vasya)
print(answer)