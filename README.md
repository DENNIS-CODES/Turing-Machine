# Turing-Machine

![image](https://user-images.githubusercontent.com/65861136/115758495-dc8c9a00-a3a7-11eb-8ae6-ade285b02897.png)

# State
By convention, Turing machine states are strings that start with q_, for example q_find, q_check or q_back, but it is also acceptable to use abbreviations such as q_f, q_c or q_b, respectively, and supply additional information as comments if necessary.

#Symbols
You may use any string as symbol, but it is advisable to use single characters as they enable passing initial sequences as strings, not tuples or lists (eg. 011 instead of ('zero', 'one', 'one')). Good choices are 0, 1, a, B, *, #, @ etc. Remember that blank symbol is denoted by [].

#Arrows
When developing algorithms, you can use <- and -> arrows to move the tape head one cell left or right, respectively. However, you may customize behaviour of head by providing a dictionary of lambdas that accept current head position index and return new index. By default, the tape is infinite in both directions.
