import os
import sys
import glob
import yaml

ALPHA = {
    "ont-r9": "/project/logsdon_shared/projects/HGSVC3/Snakemake-Flagger/config/alpha/alpha_optimum_trunc_exp_gaussian_w_16000_n_50.ONT_R941_Guppy6.3.7_DEC_2024.v1.1.0.tsv",
    "hifi": "/project/logsdon_shared/projects/HGSVC3/Snakemake-Flagger/config/alpha/alpha_optimum_trunc_exp_gaussian_w_16000_n_50.HiFi_DC_1.2_DEC_2024.v1.1.0.tsv"
}
TEMPLATE = "/project/logsdon_shared/projects/HGSVC3/Snakemake-Flagger/config_template.yaml"


def main():
    # hifi
    # ont-r9
    dtype = sys.argv[1]
    # /project/logsdon_shared/projects/HGSVC3/alignment/renamed_alignment/
    input_bam_dir = sys.argv[2]
    # /project/logsdon_shared/projects/HGSVC3/new_65_asms_renamed/
    input_asm_dir = sys.argv[3]

    with open(TEMPLATE, "rt") as fh:
        cfg = yaml.safe_load(fh)

    samples = []

    for bam in glob.glob(os.path.join(input_bam_dir, "*.bam")):
        name, _ = os.path.splitext(os.path.basename(bam))
        asm = os.path.join(input_asm_dir, f"{name}-asm-renamed-reort.fa")

        samples.append({
            "name": name,
            "asm_fa": asm,
            "bam": bam,
            "alpha": ALPHA[dtype]
        })

    cfg["samples"] = samples

    yaml.safe_dump(cfg, sys.stdout)


if __name__ == "__main__":
    raise SystemExit(main())
