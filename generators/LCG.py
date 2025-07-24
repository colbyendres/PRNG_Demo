class LCG:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m 
        self.seed = seed
        self.state = seed

    # Return the next pseudorandom number, advancing state
    def rand(self):
        self.state = (self.a * self.state + + self.c) % self.m 
        return self.state

    # Return x_i, without modifying state
    def rand_idx(self, i):
        assert self.a % self.m != 1
        a_i = pow(self.a, i, self.m)
        return (a_i * self.seed + self.c * (a_i - 1) * pow(self.a-1,-1,self.m)) % self.m