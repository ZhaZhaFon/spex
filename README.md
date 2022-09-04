
# How To

* download
```
    LibriSpeech corpus: https://www.openslr.org/12/
    WHAM! noise: https://wham.whisper.ai/
```

* environment
```
    pip install -r requirements.txt
    pip install -r prepare/requirements.txt
```

* prepare LibriMix & LibriMix-informed
```
    cd prepare/librimix && bash gen_tiny.sh
    cd prepare/librimix-informed && bash prepare_data.sh /home/zhao/data/librimix/Libri2Mix /home/zhao/code/spex+ /home/zhao/data/librimix-informed
```