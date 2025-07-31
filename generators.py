import random
import math 
import os 

class LCG:
    """
    Simple linear congruential generator
    """
    def __init__(self, a: int, c: int, m: int, seed: int):
        self.a = a
        self.c = c
        self.m = m 
        self.seed = seed
        self.state = seed

    # Return the next pseudorandom number, advancing state
    def next(self) -> int:
        self.state = (self.a * self.state + self.c) % self.m 
        return self.state
        
class MersenneTwister:
    """
    Mersenne Twister PRNG
    """
    def __init__(self, min_num, max_num):
        self.min_num = min_num 
        self.max_num = max_num 
        
    def next(self):
        # Python uses MT by default, so just use stdlib random
        return random.randint(self.min_num, self.max_num)
    
class TrueRNG:
    """
    "True" RNG, using system's random file
    """
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.num_bytes = math.ceil(int.bit_length(self.max_num - self.min_num) / 8)

    def next(self):
        return int.from_bytes(os.urandom(self.num_bytes))
    
    def next_as_bytes(self):
        return os.urandom(self.num_bytes)