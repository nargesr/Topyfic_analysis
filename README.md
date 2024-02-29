# Topyfic_analysis

This repo contains all the analysis related to [this paper](https://www.biorxiv.org/content/10.1101/2024.02.26.582178v1).

I would also encourage you to take a look at the [Topyfic package](https://github.com/mortazavilab/Topyfic).

## Overview

The gene expression profiles of distinct cell types reflect com- plex genomic interactions among multiple simultaneous 
biological processes within each cell that can be altered by disease progression as well as genetic background. 
The identification of these active cellular programs is an open challenge in the analysis of single-cell RNA-seq data. 
Latent Dirichlet Allocation (LDA) is a generative method used to identify recurring patterns in counts data, 
commonly referred to as topics that can be used to interpret the state of each cell. However, LDA’s interpretability is 
hindered by several key factors including the hyperparameter selection of the number of topics as well as the 
variability in topic definitions due to random initialization. We developed Topyfic, a Reproducible LDA (rLDA) package, 
to accurately infer the identity and activity of cellular programs in single-cell data, providing insights into the 
relative contributions of each program in individual cells. We apply Topyfic to brain single-cell and single-nucleus 
datasets of two 5xFAD mouse models of Alzheimer’s disease crossed with C57BL6/J or CAST/EiJ mice to identify distinct 
cell types and states in different cell types such as microglia. We find that 8-month 5xFAD/Cast F1 males show higher 
level of microglial activation than matching 5xFAD/BL6 F1 males, whereas female mice show similar levels of microglial 
activation. We show that regulatory genes such as TFs, microRNA host genes, and chromatin regulatory genes alone 
capture cell types and cell states. Our study highlights how topic modeling with a limited vocabulary of regulatory 
genes can identify gene expression programs in single-cell data in order to quantify similar and divergent cell states 
in distinct genotypes.

## Data
- ENCODE data: [cart](https://www.encodeproject.org/carts/5fc81d98-5a0e-4426-a9c8-10fa536430ba/)
- MODEL-AD data: [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255965)

![input data](Figures/data.png)

### Pre processing
It includes four main steps but you can download the **preprocessed gene count data** from ENOCDE portal [here]().

1. Get unfiltered gene count h5ad for each experiment
2. Merge data by experimental batch across file IDs and filter for nuclei > 500 UMI.
3. Run [Scrublet](https://www.sciencedirect.com/science/article/pii/S2405471218304745) to remove doublet cells (threshold > 0.25)
4. Annotate nuclei
5. normalize counts using [depth normalization](https://www.biorxiv.org/content/10.1101/2022.05.06.490859v1)

![ENCODE](Figures/barplot_breakdown_ENCODE.png)
![Model-AD](Figures/barplot_breakdown_ModelAD.png)

**For depth-in analysis in please look at this [github repository](https://github.com/erebboah/enc4_mouse_paper).**


### Regulatory genes
We hypothesize that we can define meaningful topics for cell identity using only regulatory genes, which account for 12% of protein coding genes.

![regulatory genes](Figures/reg_gene.png)

**For more information about how we determine regulatory genes, please look at this [github repository](https://github.com/erebboah/enc4_mouse_paper).**

## Training TopModel
To find the best number of topics (k), we start to train our model using several Ks starting from K=5 until 50.
We start our training by running on WT and 5xFAD mice separately.

For each K:
- Training model with 100 different random seeds using [topyfic.py](Training/scripts/topyfic.py) to get train object per random seed
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
Here you can find the downstream analysis related to each model

- single nucleus RNA-seq data using all genes: notebook related to this dataset and figure2 is [here](Analysis/sn_all_genes/analysing.ipynb)
- single nucleus RNA-seq data using regulatory genes: notebook related to this dataset and figure3 is [here](Analysis/sn_reg_genes/analysing.ipynb)
- single cell microglia RNA-seq data: notebook related to this dataset and figure4 is [here](Analysis/sc/analysing.ipynb)

## Hosting results

- Single-nucleus RNA-seq results: [ENCODE portal](https://www.encodeproject.org/)
- Single-cell (microglia) RNA-seq results: [Zenodo](https://zenodo.org/records/10724706?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjhlMTA4ZWFiLWQ1MjgtNGQ4Yy1iYjE5LWU5ZWY0MzM4MDVmNyIsImRhdGEiOnt9LCJyYW5kb20iOiIwZjdhNzg4ZDExMzYxMTM5MzQwODk4NGYwOWRkYzRlOSJ9.2qzF6Y7gO_RUEtQQaW7isi02FcaoxdjT664NU-pMeJJdc2ViFhRTVBi485NlHYRKXGzmrSCdZO1n8LzL0RRspg)

