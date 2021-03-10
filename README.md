# mersenne-twister-tools
A collection of various programs implementing and/or related to the Mersenne Twister PRNG. This is intended to be a bare-minimum Python 3 implementation that users can build off of.

## Features
- Seeding with any hashable type*
- Saving and restoring the state
- Pseudo-random ints and floats
- Can be used to subclass [Random](https://docs.python.org/3/library/random.html)

- Original 32-bit Mersenne Twister
- Original 64-bit Mersenne Twister
- Boost's mt11213b Mersenne Twister
- Custom Parameters Mersenne Twister

- Original 32-bit Mersenne Twister Cracker
- Original 64-bit Mersenne Twister Cracker
- Boost's mt11213b Mersenne Twister Cracker
- Custom Parameters Mersenne Twister Cracker

\*Set the environment variable `PYTHONHASHSEED = 0` to fix hashes for non-ints.
