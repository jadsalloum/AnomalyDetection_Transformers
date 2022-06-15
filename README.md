# AnomalyDetection_Transformers
Critical Applications Logs Anomaly Detection using Transformers

# Create Virutal Environment
python -m venv .venv


HDFS DataSet Location

https://zenodo.org/record/3227177/files/HDFS_1.tar.gz?download=1


# process data
python data_process.py

# run logbert
python logbert.py vocab
python logbert.py train
python logbert.py predict