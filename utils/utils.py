from math import log, gcd, sqrt
from random import randint 

# Returns true if N is a pseudoprime base a
def miller_rabin(N, s, d, a):
    val = pow(a, d, N)
    if val == 1:
        return True
    for _ in range(s):
        if val == N-1:
            return True 
        val = val * val % N 
    return False # N is composite

# Factor x = 2^s * d, where d is odd
def factor_pow2_and_odd(x):
    s, copy = 0, x-1
    while not copy & 1:
        s += 1 
        copy >>= 1
    d = x // (1 << s)
    return [s,d]

# Determines if N is prime
# Has a false positive rate <= 1-p, if ERH is not assumed
def is_prime(N, p = 0.99, assume_erh=False):
    # If ERH holds, a Miller-Rabin witness must exist <= 2 log^2(N)
    if assume_erh:
        stop = 2 * log(N) ** 2
    else:
        # At most 1/4 of Z/nZ* fail to witness when n is composite
        stop = int(log(1/(1-p), 4))
    
    s, d = factor_pow2_and_odd(N-1) 
    for _ in range(stop):
        a = randint(2, N-1)
        if not miller_rabin(N, s, d, a):
            return False 
        
    return True

# Find Miller-Rabin witness for N, returning -1 if composite
def find_witness(N):
    # Write N-1 = 2^s * d
    s, d = factor_pow2_and_odd(N)
    stop = 1+int(2 * log(N) ** 2)
    for a in range(2, stop):
        if not miller_rabin(N, s, d, a):
            return a            
    return -1 # N is probably prime

# Generate a prime with a prescribed number of digits
def generate_prime(digits, p=0.99, assume_erh=False):
    # Lower bound on probability that an odd D-digit number is prime
    # Holds when digits >= 14
    PROB_PRIME = 0.772079 / (digits-1)
    trials = int(log(1-p, 1-PROB_PRIME))

    MIN = 10 ** (digits-1) // 2
    MAX = (10 ** digits - 1) // 2 
    for _ in range(trials):
        # Ensure candidate is odd
        cand = 2 * randint(MIN, MAX) + 1
        # Cast out easy case where it's a multiple of 3
        if cand % 3 == 0:
            continue 
        if is_prime(cand, p, assume_erh):
            return cand 
        
    return -1



