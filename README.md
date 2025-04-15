# HYBSIM
This is a pyhton script to simulate hybrid genomes/genotypes between two single 
paretal genotypes (two individuals) in eigenstrat format. 
The script follows probabilistic mendelian logic for the offspring. 
Missing data (9) in one or both of the parental sources is translated into the
offspring genotype as missing data too. So beware, offspring accumulates
missingness rate from both parents.

USAGE: python HybridSimulator.py > offspring.geno
