#!/usr/bin/env python

# data
train_dir = '/home/zhao/data/librimix-informed/wav8k/min/train-100'
dev_dir = "/home/zhao/data/librimix-informed/wav8k/min/dev"
task = 'sep_clean'
sample_rate = 8000
segment = 3
segment_aux = 3

# network
nnet_conf = {
    "L": 20,
    "N": 256,
    "X": 8,
    "R": 4,
    "B": 256,
    "H": 512,
    "P": 3,
    "norm": "gLN",
    "num_spks": 1,
    "non_linear": "relu"
}

# training
epochs = 100
batch_size = 4
num_workers = 16
adam_kwargs = {
    "lr": 1e-3,
    "weight_decay": 1e-5,
}
trainer_conf = {
    "optimizer": "adam",
    "optimizer_kwargs": adam_kwargs,
    "min_lr": 1e-6,
    "patience": 8,
    "factor": 0.5,
    "logging_period": 200  # batch number
}