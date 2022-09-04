#!/bin/bash
# Copyright (c) 2021 Brno University of Technology
# Copyright (c) 2021 Nippon Telegraph and Telephone corporation (NTT).
# All rights reserved
# By Katerina Zmolikova, August 2021.

#. ../../path.sh

echo '#'
if [ $# -lt 1 ]; then
    echo '# !!! 缺少参数 (librimix_dir) !!!'
    exit 1;
fi

if [ $# -lt 2 ]; then
    echo '# !!! 缺少参数 (egs_dir) !!!'
    exit 1;
fi

librimix_dir=$1
egs_dir=$2
save_dir=$3

# Overall metadata (by Asteroid recipes)
python $egs_dir/prepare/librimix-informed/create_local_metadata.py --librimix_dir $librimix_dir --save_dir $save_dir

# Enrollment utterances for test and dev
echo '# 生成test csv...'
python $egs_dir/prepare/librimix-informed/create_enrollment_csv_fixed.py \
    $save_dir/wav8k/min/test/mixture_test_mix_both.csv \
    $egs_dir/prepare/librimix-informed/map_mixture2enrollment/wav8k/min/test/map_mixture2enrollment \
    $save_dir/wav8k/min/test/mixture2enrollment.csv
echo '# 生成dev csv...'
python $egs_dir/prepare/librimix-informed/create_enrollment_csv_fixed.py \
    $save_dir/wav8k/min/dev/mixture_dev_mix_both.csv \
    $egs_dir/prepare/librimix-informed/map_mixture2enrollment/wav8k/min/dev/map_mixture2enrollment \
    $save_dir/wav8k/min/dev/mixture2enrollment.csv

# Enrollment utterances for training
echo '# 生成train-100 csv...'
python $egs_dir/prepare/librimix-informed/create_enrollment_csv_all.py \
    $save_dir/wav8k/min/train-100/mixture_train-100_mix_both.csv \
    $save_dir/wav8k/min/train-100/mixture2enrollment.csv

#echo '# 生成train-360 csv...'
#python $egs_dir/prepare/librimix-informed/create_enrollment_csv_all.py \
#    $save_dir/wav8k/min/train-360/mixture_train-360_mix_both.csv \
#    $save_dir/wav8k/min/train-360/mixture2enrollment.csv

echo '# done.'
