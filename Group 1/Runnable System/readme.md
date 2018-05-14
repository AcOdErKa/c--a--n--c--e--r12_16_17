--DEFAULT TEXT--

FUNCTIONS FILES-
1. combination.py : compute and return next binary combination of given vector
2. encoder.py : transform an array into a single value
3. pathway_normal.py : return output vector, computing them from network consisting faults(or not faults)
4. pathway_drugged.py : return output vector, computing them from network consisting faults and drugs

CSV INPUT FILES-
1. gene.csv : contains all the proteins present in the network
2. drug.csv : contains all the drugs known

PROGRAM FILES-
1. fault_zero.py : compute all possible input vectors on faultless network, find out unique input vector
2. fault_one.py : compute all possible networks with single faults
3. fault_two.py : compute all possible networks with double faults
4. fault_three.py : compute all possible networks with triple faults **NOT MADE
5. drug_one.py : application of drugs on single faults
6. drug_two.py : application of drugs on double faults
7. drug_two2.py : application of drugs on double faults (parallelised)
8. drug_three.py : application of drugs on triple faults
9. drug_three2.py : application of drugs on triple faults (parallelised)
10. visual_drugone.py : visualise effects of drugs on single fault network
11. visual_drugtwo.py : visualise effects of drugs on double fault network
12. visual_drugthree.py : visualise effects of drugs on triple fault network **NOT MADE

CSV OUTPUT FILES-
1. output_fl.csv : DataFrame consisting of output vectors corresponding to all possible input vectors, on fault-less network
2. output_1f.csv : DataFrame consisting of output vectors corresponsing to all possible single-faulty situations
3. output_2f.csv : DataFrame consisting of output vectors corresponsing to all possible double-faulty situations
4. output_drugone.csv : DataFrame consisting of output vectors corresponding to single faults + drug application
5. output_drugtwo.csv : DataFrame consisting of output vectors corresponding to double faults + drug application
6. output_drugthree.csv : DataFrame consisting of output vectors corresponding to triple faults + drug application
