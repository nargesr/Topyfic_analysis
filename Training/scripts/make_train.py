import sys
import Topyfic
import pandas as pd
import scanpy as sc
import numpy as np

#input
k = int(sys.argv[1])

data = sc.read_h5ad("../../../data/all_ModelAD_ENCODE_control_rep1.h5ad")

main_train = Topyfic.Train(name=f"sn_ModelAD_ENCODE_allGenes_control_rep1_{k}",
                           k=k,
                           n_runs=100)
trains = []
for i in range(100):
    train = Topyfic.read_train(f"train_sn_ModelAD_ENCODE_allGenes_control_rep1_{k}_{i}.p")
    trains.append(train)
    
main_train.combine_LDA_models(data, single_trains=trains)
main_train.save_train()
