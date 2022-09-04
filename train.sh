#!/usr/bin/env bash

set -eu

#exp_dir=/home/zhao/exp-spex/baseline
exp_dir=/home/zhao/exp-spex/bsln

rm -rf $exp_dir
mkdir -p $exp_dir
python3 ./train.py --gpu "1" --checkpoint $exp_dir
