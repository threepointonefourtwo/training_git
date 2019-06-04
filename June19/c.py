
from urllib.request import urlretrieve

import pandas as pd

file  = urlretrieve('https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv','wine.csv')

df = pd.read_csv(file,sep = ";")

print(df.head())
