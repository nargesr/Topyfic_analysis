import sys
import Topyfic
import pandas as pd
import scanpy as sc
import numpy as np

#input
k = int(sys.argv[1])

data = sc.read_h5ad("../../../data/all_ModelAD_ENCODE_control_rep1.h5ad")

main_train = Topyfic.read_train(f"../train/train_sn_ModelAD_ENCODE_allGenes_control_rep1_{k}.p")

top_model, clustering, adata = Topyfic.calculate_leiden_clustering(trains=[main_train], 
							    data=data, 
							    resolution=1, 
                                                            min_cell_participation=142.725)
top_model.save_topModel()
adata.write_h5ad(f"sn_ModelAD_ENCODE_allGenes_control_rep1.h5ad")
clustering.to_csv(f"sn_ModelAD_ENCODE_allGenes_control_rep1.csv")
