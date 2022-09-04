#!/bin/bash
set -eu  # Exit on error

### TODO ###
storage_dir=/home/zhao/data/librimix
librispeech_dir=/home/zhao/database/LibriSpeech
wham_dir=/home/zhao/database/wham_noise
librimix_outdir=$storage_dir
### TODO ###

python_path=python3

### TODO ###
for n_src in 2; do
    metadata_dir=metadata/Libri$n_src"Mix-clean-100"
    $python_path scripts/create_librimix_from_metadata.py --librispeech_dir $librispeech_dir \
        --wham_dir $wham_dir \
        --metadata_dir $metadata_dir \
        --librimix_outdir $librimix_outdir \
        --n_src $n_src \
        --freqs 8k 16k \
        --modes min max \
        --types mix_clean mix_both mix_single
done
### TODO ###