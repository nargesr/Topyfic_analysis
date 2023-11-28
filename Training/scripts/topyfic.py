import sys
import Topyfic
import pandas as pd
import scanpy as sc
import numpy as np
import random

#input
k = int(sys.argv[1])
random_state = int(sys.argv[2])

data = sc.read_h5ad("../../../data/all_ModelAD_ENCODE_control_rep1.h5ad")

train = Topyfic.Train(name=f"sn_ModelAD_ENCODE_allGenes_control_rep1_{k}_{random_state}",
                      k=k,
                      n_runs=1,
                      random_state_range=[random_state])
train.run_LDA_models(data, batch_size=128, max_iter=5, n_jobs=1, n_thread=1)
train.save_train()

