import os
import pandas as pd

def Load_HDFS_Data(logfile):
    df = pd.read_csv(logfile, engine='c', na_filter=False, memory_map=True, dtype={'Date':object, "Time": object})
    return df

