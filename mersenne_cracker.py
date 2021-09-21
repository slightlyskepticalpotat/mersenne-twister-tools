from mersenne_twister import MersenneTwister

class MersenneCracker:
    def __init__(self, variant = "mt19937", parameters = []):
        if variant == "mt19937":  # 32-bit version of original twister
            self.w = 32
            self.n = 624
            self.m = 397
            self.r = 31
            self.a = 0x9908b0df
            self.u = 11
            self.d = 0xffffffff
            self.s = 7
            self.b = 0x9d2c5680
            self.t = 15
            self.c = 0xefc60000
            self.l = 18
            self.f = 1812433253
        elif variant == "mt19937_64":  # 64-bit version of original twister
            self.w = 64
            self.n = 312
            self.m = 156
            self.r = 31
            self.a = 0xb5026f5aa96619e9
            self.u = 29
            self.d = 0x5555555555555555
            self.s = 17
            self.b = 0x71d67fffeda60000
            self.t = 37
            self.c = 0xfff7eee000000000
            self.l = 43
            self.f = 6364136223846793005
        elif variant == "mt11213b":  # mt11213b twister version from boost
            self.w = 32
            self.n = 351
            self.m = 175
            self.r = 19
            self.a = 0xccab8ee7
            self.u = 11
            self.d = 0xffffffff
            self.s = 7
            self.b = 0x31b6ab00
            self.t = 15
            self.c = 0xffe50000
            self.l = 17
            self.f = 1812433253
        elif variant == "custom":  # only use if you know what you're doing
            assert len(parameters) == 13
            self.w = parameters[0]
            self.n = parameters[1]
            self.m = parameters[2]
            self.r = parameters[3]
            self.a = parameters[4]
            self.u = parameters[5]
            self.d = parameters[6]
            self.s = parameters[7]
            self.b = parameters[8]
            self.t = parameters[9]
            self.c = parameters[10]
            self.l = parameters[11]
            self.f = parameters[12]
        else:
            raise NotImplementedError
        self.lower_mask = int("1" * self.r, 2)
        self.upper_mask = int("1" * (self.w - self.r) + "0" * self.r, 2)

    def crack_state(self, outputs):
        self.original_state = [0] * self.n
        assert len(outputs) >= self.n
        assert all(isinstance(i, int) for i in outputs)
        outputs = outputs[:self.n]
        for i in range(self.n):  # reverses the temper operations
            y = outputs[i]
            y = self.untemper_right(y, self.l)
            y = self.untemper_left(y, self.t, self.c)
            y = self.untemper_left(y, self.s, self.b)
            y = self.untemper_right_mask(y, self.u, self.d)
            self.original_state[i] = y
        return self.original_state

    def untemper_right(self, n, shift):
        i = 0
        while i * shift < self.w:
            new_mask = n & (((((1 << self.w) - 1) << (self.w - shift)) & ((1 << self.w) - 1)) >> (shift * i))
            n ^= new_mask >> shift
            i += 1
        return n

    def untemper_right_mask(self, n, shift, mask):
        i = 0
        while i * shift < self.w:
            new_mask = n & (((((1 << self.w) - 1) << (self.w - shift)) & ((1 << self.w) - 1)) >> (shift * i))
            new_mask >>= shift
            n ^= new_mask & mask
            i += 1
        return n

    def untemper_left(self, n, shift, mask):
        i = 0
        while i * shift < self.w:
            new_mask = n & ((((1 << self.w) - 1) >> (self.w - shift)) << (shift * i))
            new_mask <<= shift
            n ^= new_mask & mask
            i += 1
        return n

    def untwist(self, state):  # returns the past state before a twist
        state = list(state)
        for i in range(self.n - 1, -1, -1):
            temp = state[i] ^ state[(i + self.m) % self.n]  # find leading bit
            if temp % 2:
                temp ^= self.a
            shifted = (temp << 1) & self.upper_mask
            temp = state[(i - 1) % self.n] ^ state[(i + self.m - 1) % self.n]  # ending bits of int
            if temp & self.upper_mask == self.upper_mask:  # check if leading bit is the same
                temp ^= self.a
                shifted |= 1
            state[i] = shifted ^ (temp << 1) & self.lower_mask
        return state

if __name__ == "__main__":
    # this can also be used to crack floats if you scale and round them first
    random_32 = MersenneTwister()
    old_state_32 = random_32.getstate()
    outputs_32 = [random_32.random_integer() for _ in range(624)]
    cracker_32 = MersenneCracker()
    new_state_32 = cracker_32.crack_state(outputs_32)
    random_32.setstate([new_state_32, 0])  # start at beginning of state
    assert outputs_32 == [random_32.random_integer() for _ in range(624)]
    print("32-bit Successfully Cracked")
    assert cracker_32.untwist(new_state_32)[1:] == old_state_32[0][1:]  # seed may be different
    print("32-bit Successfully Reversed")

    random_32_alt = MersenneTwister(variant = "mt11213b")
    outputs_32_alt = [random_32_alt.random_integer() for _ in range(624)]
    cracker_32_alt = MersenneCracker(variant = "mt11213b")
    new_state_32_alt = cracker_32_alt.crack_state(outputs_32_alt)
    random_32_alt.setstate([new_state_32_alt, 0])  # start at beginning of state
    assert outputs_32_alt == [random_32_alt.random_integer() for _ in range(624)]
    print("32-bit Alt Successfully Cracked")

    random_64 = MersenneTwister(variant = "mt19937_64")
    outputs_64 = [random_64.random_integer() for _ in range(312)]
    cracker_64 = MersenneCracker(variant = "mt19937_64")
    new_state_64 = cracker_64.crack_state(outputs_64)
    random_64.setstate([new_state_64, 0])  # start at beginning of state
    assert outputs_64 == [random_64.random_integer() for _ in range(312)]
    print("64-bit Successfully Cracked")
