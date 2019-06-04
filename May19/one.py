#!/usr/bin/env python3

from urllib.request import urlretrieve
import pandas as pd

url =  "https://archive.ics.uci.edu/ml/machine-learning-databases/00477/Real%20estate%20valuation%20data%20set.xlsx";

urlretrieve(url,'real_estate.xlsx');

#pd.read_csv('real_estate.csv');


