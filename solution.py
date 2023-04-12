import scipy.stats as stats
import pandas as pd
import numpy as np


chat_id = 263008738 

def solution(sample) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    t_stat, p_value = stats.ttest_1samp(sample, 500)
    alpha = 0.06
    if p_value < alpha:
        reject_null_hypothesis = True
    else:
        reject_null_hypothesis = False
    return reject_null_hypothesis # Ваш ответ, True или False
