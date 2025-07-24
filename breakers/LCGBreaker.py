import sys
from generators.LCG import LCG
import math 
import numpy as np
import matplotlib.pyplot as plt

def recover_modulus(num_x, gen):
    """
    Attempt to recover the modulus m, using num_x consecutive observations
    """
    assert num_x > 3
    x_vals = [gen.rand() for _ in range(num_x)]
    diffs = [x_vals[i+1] - x_vals[i] for i in range(num_x-1)]
    m_mults = [abs(diffs[i+1]**2-diffs[i]*diffs[i+2]) for i in range(num_x-3)]

    # Test all pairs and take the smallest positive gcd
    m = math.inf
    for i in range(num_x-3):
        for j in range(i+1, num_x-3):
            new_m = math.gcd(m_mults[i], m_mults[j])
            if new_m == 0:
                continue 
            m = min(new_m, m)

    return m

def test_modulus_recovery(gen, x_vals, num_attempts=100):
    success_rates = []
    true_m = gen.m
    for num_x in x_vals:
        successes = 0
        for _ in range(num_attempts):
            m = recover_modulus(num_x, gen)
            if m == true_m:
                successes += 1
        success_rates.append(1.0 * successes / num_attempts)
    
    plt.plot(x_vals, success_rates)
    plt.title('Success Rate vs # Observed Outputs')
    plt.xlabel('# of Observed Outputs')
    plt.ylabel('Success Rate')
    plt.xticks(x_vals)
    plt.savefig('plots/lcg_break_rate.png')

m = 2 ** 32
a = 1664525
c = 1013904223
gen = LCG(a, c, m, 33)
x_vals = [i for i in range(8, 15)]
test_modulus_recovery(gen, x_vals)