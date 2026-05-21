# Snakemake-Flagger
Workflow to run base Flagger v1.1.0 w/o alignment.
* https://github.com/mobinasri/flagger/tree/main


## Getting Started
Requires snakemake and apptainer 

```bash
git clone https://github.com/logsdon-lab/Snakemake-Flagger.git
cd Snakemake-Flagger
```

## Config

```yaml
#Output benchmarks directory
benchmarks_dir: benchmarks
#Output logs directory
logs_dir: logs
#Output results directory
output_dir: results
samples:
  #HMM-Flagger config
- alpha: config/alpha/alpha_optimum_trunc_exp_gaussian_w_16000_n_50.HiFi_DC_1.2_DEC_2024.v1.1.0.tsv
  #Genome assembly fasta file + index file
  asm_fa: test/test.fa
  #Bam file
  bam: test/test.bam
  #Unique identifier
  name: Test
  #Annotation directory
  bias_annot_dir: test/annotations
  #Generate conservative.bed (optional)
  conservative_bed: True
```
## Test

To run a dry run 

```bash
snakemake -p --configfile test/test.yaml -n 
```