#!/usr/bin/env python3

import numpy as np

data = np.loadtxt('comma.txt',delimiter = ',',skiprows = 1,usecols = [0,1,2])

print(data)
