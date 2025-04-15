#!/usr/bin/env python3

"""
Simulate hybrid offspring between two genotypes in EIGENSTRAT format.
USAGE: python script.py > output
"""

import numpy as np

# Load parental genotype data (EIGENSTRAT format, 1 char per genotype)
file1 = np.genfromtxt("parent1.geno", dtype='int', delimiter=1)
file2 = np.genfromtxt("parent1.geno", dtype='int', delimiter=1)

# Check that both files have the same number of SNPs
if file1.size != file2.size:
    raise ValueError("Input files must have the same number of SNPs.")

# Initialize offspring array with 9 (missing data) by default
offspring = np.full(file1.shape, 9, dtype=int)

# Homozygous matches
mask_00 = (file1 == 0) & (file2 == 0)
mask_22 = (file1 == 2) & (file2 == 2)
offspring[mask_00] = 0
offspring[mask_22] = 2

# Heterozygous (0,2) or (2,0) => 1
mask_02_20 = ((file1 == 0) & (file2 == 2)) | ((file1 == 2) & (file2 == 0))
offspring[mask_02_20] = 1

# Both heterozygous (1,1) => probabilistic [0,1,1,2] (25%, 50%, 25%)
mask_11 = (file1 == 1) & (file2 == 1)
rand_vals = np.random.randint(4, size=mask_11.sum())
offspring[mask_11] = np.select(
    [rand_vals == 0, (rand_vals == 1) | (rand_vals == 2), rand_vals == 3],
    [0, 1, 2]
)

# (0,1) or (1,0) => random [0,1]
mask_01_10 = ((file1 == 0) & (file2 == 1)) | ((file1 == 1) & (file2 == 0))
rand_vals = np.random.randint(2, size=mask_01_10.sum())
offspring[mask_01_10] = rand_vals

# (1,2) or (2,1) => random [1,2]
mask_12_21 = ((file1 == 1) & (file2 == 2)) | ((file1 == 2) & (file2 == 1))
rand_vals = np.random.randint(2, size=mask_12_21.sum())
offspring[mask_12_21] = rand_vals + 1

# Save result to file
with open("offspring_file.geno", "w") as f:
    for val in offspring:
        f.write(str(val))

