from tsmsim import Algorithm
from tsmsim import generate_words

Algorithm({
    'q_s': {
        '[]': True,
        'a': ('#', 'q_1', '->'),
        'b': False,
        '*': ('q_c', '->'),
    },
    'q_1': {
        'a': '->',
        '*': '->',
        'b': ('*', 'q_b', '<-'),
        '[]': False,
    },
    'q_b': {
        'a': '<-',
        '#': ('q_s', '->'),
        '*': '<-',
    },
    'q_c': {
        '*': '->',
        'a': False,
        'b': False,
        '[]': True,
    }
}).test(
    generate_words('ab', 10),
    lambda word: word == '0' * (len(word) // 2) + '1' * (len(word) // 2)
)