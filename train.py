#!/usr/bin/env python
import os
import pprint
import argparse
import random
import torch

from libs import utils
import conf

logger = utils.get_logger(__name__)

import os 
os.environ['CUDA_LAUNCH_BLOCKING']="1"

def run(args):

    gpuids = tuple(map(int, args.gpus.split(",")))
    
    import data
    print('>> 加载train_set...')
    train_set = data.LibriMixInformed(
        csv_dir=conf.train_dir,
        task=conf.task,
        sample_rate=conf.sample_rate,
        segment=conf.segment,
        segment_aux=conf.segment_aux,
    )
    print('>> 加载dev_set...')
    dev_set = data.LibriMixInformed(
        csv_dir=conf.dev_dir,
        task=conf.task,
        sample_rate=conf.sample_rate,
        segment=conf.segment,
        segment_aux=conf.segment_aux,
    )
    print('')

    from torch.utils.data import DataLoader
    print('>> 加载train_loader...')
    train_loader = DataLoader(train_set,
                              shuffle=True,
                              batch_size=conf.batch_size,
                              num_workers=conf.num_workers,
                              drop_last=True)
    print('>> 加载dev_loader...')
    dev_loader = DataLoader(dev_set,
                            shuffle=True,
                            batch_size=conf.batch_size,
                            num_workers=conf.num_workers,
                            drop_last=True)

    print('>> 加载model网络结构')
    from nnet import conv_tas_net
    model = conv_tas_net.ConvTasNet(**conf.nnet_conf)

    print('>> 加载trainer')
    from libs import trainer
    trainer = trainer.SiSnrTrainer(model,
                                   gpuid=gpuids,
                                   checkpoint=args.checkpoint,
                                   resume=args.resume,
                                   **conf.trainer_conf)
    
    print('')
    print(' ### START TRAINING ###')
    trainer.run(train_loader, dev_loader, num_epochs=conf.epochs)
    print(' ### TRAINING DONE ###')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=
        "Command to start ConvTasNet training, configured from conf.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--gpus",
                        type=str,
                        default="0,1",
                        help="Training on which GPUs "
                        "(one or more, egs: 0, \"0,1\")")
    parser.add_argument("--checkpoint",
                        type=str,
                        required=True,
                        help="Directory to dump models")
    parser.add_argument("--resume",
                        type=str,
                        default="",
                        help="Exist model to resume training from")
    args = parser.parse_args()
    logger.info("Arguments in command:\n{}".format(pprint.pformat(vars(args))))

    torch.backends.cudnn.enable =True
    torch.backends.cudnn.benchmark = True
    
    print('')
    run(args)
