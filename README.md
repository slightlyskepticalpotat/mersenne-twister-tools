# mersenne-twister-tools
A collection of various programs implementing and/or related to the Mersenne Twister PRNG. This is intended to be a bare-minimum Python 3 (minimum version 3.6, as format strings are used) implementation that users can build off of.

## Features
- Seeding with any hashable type*
- Saving and restoring the state
- Pseudo-random ints and floats
- Can be used to subclass [Random](https://docs.python.org/3/library/random.html)
- Derive past generated numbers


- Original 32-bit Mersenne Twister
- Original 64-bit Mersenne Twister
- Boost's mt11213b Mersenne Twister
- Custom Parameters Mersenne Twister


- Original 32-bit Mersenne Twister Cracker
- Original 64-bit Mersenne Twister Cracker
- Boost's mt11213b Mersenne Twister Cracker
- Custom Parameters Mersenne Twister Cracker

\*Set the environment variable `PYTHONHASHSEED = 0` to fix hashes for non-ints.

## Testing
`mersenne_twister.py` and `mersenne_cracker.py` both run tests when you run them from the command line.
```bash
$ python3 mersenne_cracker.py
$ python3 mersenne_twister.py
```

## Contributing
Please report any bugs that you encounter, and open a pull request if you have something to add to the program. Thank you!

## References
When I was creating this program, I found several resources that are useful for anyone seeking to understand the Mersenne Twister. They are listed here for reference:
- https://en.wikipedia.org/wiki/Mersenne_Twister
- http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/emt.html
- https://sci-hub.se/10.1145/272991.272995
- http://www.quadibloc.com/crypto/co4814.htm
- https://jazzy.id.au/2010/09/22/cracking_random_number_generators_part_3.html
- https://www.boost.org/doc/libs/1_77_0/doc/html/boost_random/reference.html#boost_random.reference.generators