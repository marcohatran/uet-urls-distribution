import gzip
import os
import sys

import pyarrow as pa
import json
import pyarrow.parquet as pq
import numpy as np
import pandas as pd
from json2parquet import load_json, ingest_data, write_parquet, write_parquet_dataset
from pandas.io.json import json_normalize

from config.config_project import folder_output_path
from helper.reader_helper import get_files_in_folder


def load_parquet(file_parquet):
    parquet_file = pq.ParquetFile(file_parquet)
    df = pd.read_parquet(file_parquet)
    # df.loc[df['uid'] == '522684655'].describe()
    # print(parquet_file.metadata)
    # print(parquet_file.schema)
    # print(df.head())
    # print(df.columns.tolist())
    # print(df.describe())
    return df
