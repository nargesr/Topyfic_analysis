# Topyfic_analysis

This repo contains all the analysis related to [this paper]().

## Overview
The gene expression profile of cell types results from complex interactions among biological processes within those cells. 
Identifying the distinct cellular programs active in a cell is an open challenge for the analysis of single-cell RNA-seq data. 
Latent Dirichlet Allocation (LDA) is commonly used to identify recurring patterns in count data, commonly referred to as topics. 
Grade of membership (GoM) for each LDA topic can then be assigned back to samples, such as each cell. 
However, LDA's interpretability is hindered by hyperparameter selection of the number of topics as well as the variability in topic definitions due to random initialization. 
We developed Topyfic, a Reproducible LDA (rLDA) package, to accurately infer the identity and activity of cellular programs in single-cell data, providing insights into the relative contributions of each program in individual cells. 
We apply Topyfic to brain single-cell and single-nucleus datasets from mouse models of AD to identify distinct cell types and states in cell types such as microglia. 
We show that regulatory genes such as TFs, microRNA host genes, and chromatin regulatory genes alone capture much of these topics. 
Our study highlights the potential of topic modeling using regulatory genes for elucidating biological structure in RNA-seq gene expression data.

## Data
- ENCODE data: [cart](https://www.encodeproject.org/carts/5fc81d98-5a0e-4426-a9c8-10fa536430ba/)
- MODEL-AD data: comming soon

## Pre processing
It includes four main steps but you can download the **preprocessed gene count data** from ENOCDE portal [here]().

1. Get unfiltered gene count h5ad for each experiment
2. Merge data by experimental batch across file IDs and filter for nuclei > 500 UMI.
3. Run [Scrublet](https://www.sciencedirect.com/science/article/pii/S2405471218304745) to remove doublet cells (threshold > 0.25)
4. Annotate nuclei
5. normalize counts using [depth normalization](https://www.biorxiv.org/content/10.1101/2022.05.06.490859v1)


### Regulatory genes


## Training TopModel
To find the best number of topics (k), we start to train our model using several Ks starting from K=5 until 50.
We start our training by running on WT and 5xFAD mice separately.

For each K:
- Training for 100 random seeds: Run [run.sh](Training/scripts/run.sh) to get train object per random seed
- Aggregate all training objects using [make_train.py](Training/scripts/make_train.py)
- Make TopModel using [make_topmodel.py](Training/scripts/make_topmodel.py)

At the end you have one train object, one Topmodel object for each K.


### Description of each folder in Training directory

- Training on WT (BL6 and BL6/CAST) using all genes: [here](Training/sn_allgenes_control_train_rep1).
- Training on 5xFAD (BL6 and BL6/CAST) using all genes: [here](Training/sn_allgenes_5xFAD_train_rep1).
- Combine training using all genes: [here](Training/sn_allgenes_5xFAD_control_combine).

- Training on WT (BL6 and BL6/CAST) using regulatory genes: [here](Training/sn_reggenes_control_train_rep1).
- Training on 5xFAD (BL6 and BL6/CAST) using regulatory genes: [here](Training/sn_reggenes_5xFAD_train_rep1).
- Combine training using regulatory genes: [here](Training/sn_reggenes_5xFAD_control_combine).

- Training on microglia single cell  using all genes: [here](Training/sc_microgllia).


## Analysis TopModel
