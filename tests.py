from generators import *
from random import *
import numpy as np
from scipy.stats import chisquare
import time 
import os

# Generate random values for our test
def gen_vals(gen, num_vals):
    vals = np.empty(num_vals).astype(np.uint32)
    for i in range(num_vals):
        vals[i] = gen.next()
    return vals 

# Run a goodness-of-fit test against the uniform distribution
def chi_square_test(values, bins=256):
    hist, _ = np.histogram(values, bins=bins, range=(0, 1 << 32))
    if np.any(hist < 5):
        print("Warning: Some bins have <5 samples — chi-squared may be unstable.")
    expected = len(values) / bins
    chi2, p = chisquare(hist, f_exp=[expected]*bins)
    return chi2, p

# Generates count integers from a given generator
# This is stored as a bitstring, which is then written to a file for NIST battery
def generate_bits(gen, count: int, filename: str):
    bytes = bytearray()
    for _ in range(count):
        x = int(gen.next())
        bytes.extend(x.to_bytes(4, 'big'))  # 32-bit output
    bits = ''.join(f'{byte:08b}' for byte in bytes)
    with open(os.path.join('NIST',filename), 'w') as fp:
        fp.write(bits)

if __name__ == '__main__':
    NUM_GENERATORS = 3
    m = 1 << 32
    a = 1664525
    c = 1013904223
    
    seed = time.time()
    TRIALS = 10 ** 6
    generators = [LCG(a, c, m, seed), MersenneTwister(0, m), TrueRNG(0, m-1)]
    chi_stat = []
    p_vals = []
    for gen in generators:
        vals = gen_vals(gen, TRIALS)
        chi2, p = chi_square_test(vals)
        chi_stat.append(chi2)
        p_vals.append(p)
        
    print(f'chi statistics: {chi_stat}')
    print(f'p values: {p_vals}')