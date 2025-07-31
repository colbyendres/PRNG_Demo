# Overview
This is a simple demonstration of various PRNGs implemented in Python. We implement a simple LCG, MT19937 Mersenne Twister, and the host's CSPRNG (i.e. `/dev/random` for Unix). We also perform goodness-of-fit tests for checking uniformity and test against the NIST randomness suite.

# Build Instructions
From a fresh Python virtual environment:
```
pip install -r requirements.txt
```
The chi-squared test for uniformity and attempts can now be ran as simple Python scripts. If you want to test against the NIST battery, you'll need to output the generated numbers as raw bits to a `*.txt` file.
## Building NIST
The binaries for running the NIST suite can be built as follows:
```
cd NIST
make
```
Suppose you have a file called `foo.txt` containing $n$ bits within your current directory. The suite can be ran by:
```
./assess n
```
which prompts the user for further configuration. For further information, see [here](https://csrc.nist.gov/projects/random-bit-generation/documentation-and-software)



