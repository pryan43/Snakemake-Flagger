# Snakemake-Flagger
Workflow to run base Flagger v1.1.0 w/o alignment.
* https://github.com/mobinasri/flagger/tree/main

```bash
module load singularity
snakemake -p --configfile config/config_ont-r9.yaml --sdm apptainer --workflow-profile ~/profiles/lpc/ -j 50 --apptainer-args "--bind '/project/logsdon_shared'"
```
