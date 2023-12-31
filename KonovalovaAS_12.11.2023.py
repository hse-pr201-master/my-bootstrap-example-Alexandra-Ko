# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pB4zM1pBOOCX0zezlYGMpWFLt3uk4Sn_
"""

import numpy as np
import pandas as pd
import seaborn as sns

!pip install arch

from arch.bootstrap import IIDBootstrap, IndependentSamplesBootstrap

import scipy.stats as sts

x=sts.bernoulli(0.5).rvs(100)
x

np.mean(x)

[np.quantile(x, 0.025), np.quantile(x, 0.975)]

boot_x = IIDBootstrap(x, seed=111111)
boot_x.conf_int(np.mean, method='percentile', reps=10000, size=0.95)

x1=sts.bernoulli(0.8).rvs(225)
x2=sts.bernoulli(0.6).rvs(100)

def mean_diff(x, y):
  return np.mean(x) - np.mean(y)

boot_xy = IndependentSamplesBootstrap(x1, x2, seed=111111)
boot_xy.conf_int(mean_diff, reps=10000, size=0.95, method='basic')