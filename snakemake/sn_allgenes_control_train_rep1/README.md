# single-nucleus WT training 

Traing Topyfic using (a) 1 male replicate and 1 female replicate of WT mice from both genotypes (4 mice) using all genes 


## Run in SLURM:

```
snakemake \
-j 1000 \
--latency-wait 300 \
--use-conda \
--rerun-triggers mtime \
--executor cluster-generic \
--cluster-generic-submit-cmd \
"sbatch -A model-ad_lab \
  --partition=highmem \
  --cpus-per-task 16 \
  --mail-user=nargesr@uci.edu \
  --mail-type=START,END,FAIL \
  --time=00:10:00" \
-n \
-p \
--verbose
```
