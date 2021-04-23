# Turing-Machine
The Turing machine is not a machine. It is a mathematical model, which was formulated by the English mathematician `Alan Turing` in 1936.

![image](https://user-images.githubusercontent.com/65861136/115758495-dc8c9a00-a3a7-11eb-8ae6-ade285b02897.png)

# Implementation of a TM in Python
- We implement a Turing Machine in Python as a class. We define another class for the `read/write` tape of the Turing Machine. The core of the tape inside the class Tape is a `dictionary`, which contains the `entries` of the tape. This way, we can have `negative indices`. A `Python list` is not a convenient `data structure`, because Python lists are bounded on one side, i.e. `bounded by 0`.

- We define the method `__str__(self)` for the `class Tape` .` __str__(self)` is called by the built-in `str()` function. The `print` function uses also the `str` function to calculate the `"informal"` string representation of an object, in our case the tape of the `TM`. The method `get_tape()` of our class TuringMachine makes use of the `str` representation returned by `__str__.`

- With the aid of the method `__getitem__()`, we provide a reading access to the tape via indices. The definition of the method `__setitem__()` allows a writing access as well, as we can see e.g. in the statement
`self.__tape[self.__head_position] = y[1]`
of our class TuringMachine implementation.

- The class TuringMachine:
We define the method `__str__(self)`, which is called by the `str()` built-in function and by the print statement to compute the "informal" string representation of an object, in our case the string representation of a tape

## Algorithms
Formally, Turing machine is a tuple of input alphabet, tape alphabet, set of states, transition function, initial state, accepting state, rejecting state and blank symbol. By default,

initial state `(qs)` is denoted by `q_s,`
accepting state `(qy)` is denoted by `q_y` or `True,`
rejecting state `(qn)` is denoted by `q_n` or `False`,
blank symbol `(□)` is denoted by `[]`.
The tape alphabet and the set of states are inferred from the `transition function`. It is also assumed that the input alphabet contains all symbols from working alphabet and does not contain blank symbol. Therefore, in most cases it is only required to define the `transition function`.

You may create an Algorithm object by passing a `dictionary of dictionaries` to the constructor. The keys of the outer dictionary are states, the keys of inner dictionaries are symbols, and the values of inner dictionaries represent the transition function values. For example,

```
Algorithm({
    'q_s': {
        '[]': True,
        '0': ('#', 'q_1', '->'),
        '1': False,
        '*': ('q_c', '->'),
    },
    # etc.
})
```
specifies that if `q_s` is the current state, the machine will either

- change state to `True (accepting state)`, if the current symbol is `[] (blank)`,
- replace current symbol with `#`, change state to `q_1`, and move one cell to the `right`, if the current symbol is `0`,
- change state to `False (rejecting state)`, if the current symbol is `1`, or
- change state to `q_c` and move one cell to the `right`, if the current symbol is `*`.
- Note that there is no obligation for a transition function value to be a `triple (state, symbol, arrow)`, since the missing elements will be interpreted as remaining the current state, not changing the current symbol, or not moving the tape head, respectively. You may also replace tuples of single element, for instance `('->',),` with the element itself, that is `'->'`. This trick is especially useful in case of arrows or `final states`.

# State
By convention, Turing machine states are strings that start with `q_`, for example `q_find`, `q_check` or `q_back`, but it is also acceptable to use abbreviations such as `q_f`, `q_c` or `q_b`, respectively, and supply additional information as comments if necessary.

# Symbols

You may use any string as symbol, but it is advisable to use single characters as they enable passing initial sequences as `strings`, not `tuples` or `lists` (eg. `011` instead of `('zero', 'one', 'one'))`. Good choices are `0, 1, a, B, *, #, @` etc. Remember that blank symbol is denoted by `[]`.

# Arrows
```
arrows={
    '<-': lambda x: x-1,
    '->': lambda x: x+1,
}
```
When developing algorithms, you can use `<-` and `->` arrows to move the tape head one cell `left or right`, respectively. However, you may customize behaviour of head by providing a dictionary of lambdas that accept current head position index and return new index. By default, the tape is infinite in both directions.

## Running
You may execute your algorithm for single input by calling run method on Algorithm object. The following code will instantiate a new Turing machine with given input as initial sequence and also print all configurations one by one until machine terminates or step limit is exceeded.
```
Algorithm({
    'q_s': {
        '0': ('1', '->'),
        '1': ('0', '->'),
        '[]': True,
    }
}).run('001011001')
```
You may also customize this behaviour by passing additional keyword arguments. The machine terminates when it reaches any state from the final_states dictionary keys. If that happens, run method returns dictionary value for reached state. By default, you may use `q_y` or `True` as accepting state in order for run method to `return True`, and `q_n` or `False` as `rejecting state` in order to return `False`.

```
final_states={
    True: True,
    False: False,
    'q_y': True,
    'q_n': False,
}
```

Some algorithms may occasionally fall into an `infinite loop`. You may limit maximum step number by adjusting `step_limit`. You may also pass None to disable this feature. When step limit is reached, `an error` will be raised if `raise_on_exceed` is set to `True`, otherwise `None` will be returned. By default,

```
step_limit=1_000_000,
raise_on_exceed=True
```

If you need only final result, you may turn off logging by setting print_configurations keyword argument to `False`. By default,

```
print_configurations=True
```
## Testing
You may run the test suite by calling test method on Algorithm object. This method requires two arguments: an iterable of initial sequences `(tuple, list, generator etc.)` and a function that returns expected output `(True, False, or another value from results_states dictionary)`. Note that you may pass either lambda or name of function/method defined with `def keyword`.

```
Algorithm({
    # write your algorithm here
}).test(
    generate_words('01', 10),
    lambda word: len(word) % 2 == 0
)
```

You may use generate_words function to generate all words from supplied set of symbols of given maximum length. Note that you may also use itertools.chain in order to merge multiple test suites into a single one.
