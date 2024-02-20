# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:28:15 2023

@author: Mohamed Arafa
"""
import glassdoor_scraper as gs 
import pandas as pd 



df = gs.get_jobs('data scientist',1000,False, 30)

df.to_csv('glassdoor_jobs01.csv', index = False)

df
