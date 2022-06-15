

from Load_Data import Load_HDFS_Data


if __name__ == '__main__':
    df = Load_HDFS_Data('./Datasets/HDFS.log')

    print(df.head())
