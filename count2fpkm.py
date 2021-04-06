import numpy as np
import pandas as pd

import seaborn as sns
from plotnine import *

# read count matrix and gene length data
count_matrix = pd.read_csv('count_matrix.csv', sep=',', index_col='gene')
GID_length = pd.read_csv('Total_GID_length.txt', sep='\t', index_col='GID')

# get needed indexes and their lengths
indexes = count_matrix.index.tolist()
gene_length = GID_length.loc[indexes]['Length']

# define FPKM formula
def fpkm(col):
    sum_col = np.sum(col)
    return col/gene_length/sum_col*1e9

# convert count to FPKM
fpkm_matrix = count_matrix.apply(fpkm, axis=0).astype(int)

# output the fpkm matrix
fpkm_matrix.to_csv('fpkm_matrix.csv', sep=',', header=True, index=True)

