## dvc stage

dvc stage add -n <stage-name> \
    -d <dependency> \
    -o <output> \
    -p <parameter> \
    -M <metrics> \ 
    <commmand-to-run>

dvc stage add -n preprocess \
    -d src/preprocess.py -d data/raw.csv \
    -o data/processed.csv \
    python src/preprocess.py data/raw.csv data/processed.csv

dvc stage add -n train_model \
    -d src/train.py -d data/processed.csv -p train.features,train.target \
    -o models/model.pkl -M metrics/score.txt \
    python src/train.py data/processed.csv models/model.pkl metrics/score.txt