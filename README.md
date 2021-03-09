# mersenne-twister-tools
A collection of various programs implementing and/or related to the Mersenne Twister PRNG. This is intended to be a bare-minimum Python 3 implementation that users can build off of.

## Features
- Original 32-bit Mersenne Twister
- Original 64-bit Mersenne Twister
- Boost's mt11213b Mersenne Twister
- Custom Parameters Mersenne Twister
- Seeding with any hashable type*
- Saving and restoring the state

\*Set the environment variable `PYTHONHASHSEED = 0` to fix hashes for non-ints.
