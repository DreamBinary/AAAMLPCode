# -*- coding:utf-8 -*-
# @FileName : tmp.py
# @Time : 2024/2/26 20:14
# @Author : fiv


import pandas as pd
from sklearn import datasets

data = datasets.fetch_openml(
    "mnist_784",
    version=1,
    return_X_y=True
)
pixel_values, targets = data
pixel_values.reshape()