python3 model-development/generate-training-data.py $1
python3 model-development/train-linear-model.py > static/predictor-lr.pkl
python3 model-development/train-sgd-model.py > static/predictor-gd.pkl
rm cases.csv

