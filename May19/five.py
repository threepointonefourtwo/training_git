#!/usr/bin/env python3

# import flat file using pandas

import pandas as pd

df = pd.read_csv('winequality-white.csv')

print(df.head())

axle = pd.read_excel('real.xlsx')

print(axle.head())
