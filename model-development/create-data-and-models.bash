python3 generate-training-data.py $1
python3 train-linear-model.py
python3 train-sgd-model.py
rm cases.csv

