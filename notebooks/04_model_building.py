# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 01:05:19 2023

@author: Mohamed Arafa
"""

#Paths 

MLFLOW_TRACKING_URI = r'../models/mlruns'
MLFLOW_EXPERIMENT_NAME = "salary_estimator"

LOG_PATH = r"C:\Users\Mohamed Arafa\Salary_Estimator\models"
LOG_DATA_PKL    =  "data.pkl"
LOG_MODEL_PKL   =  "model.pkl"
LOG_METRICS_PKL =  "metrics.pkl"
DATAPATH=r"C:\Users\Mohamed Arafa\Salary_Estimator\data\raw"
PROCESSEDPATH=r"C:\Users\Mohamed Arafa\Salary_Estimator\data\processed"
PLOTPATH=r"C:\Users\Mohamed Arafa\Salary_Estimator\reports\figures"
#import Packages 

import pandas as pd 
import numpy as np
import logging
import pickle
import random
import plotly 
import os
from pathlib import Path
import matplotlib.pyplot as plt


import mlflow
from mlflow.tracking import MlflowClient

from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.pipeline import make_pipeline, FeatureUnion
from sklearn.feature_selection import VarianceThreshold
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error
from sklearn.decomposition import PCA, KernelPCA
from sklearn import tree
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV


import statsmodels.api as sm


df=pd.read_csv(os.path.join(PROCESSEDPATH,"EDA_glassdoor_jobs.csv"))

#choose relavent cols 

df.columns
df_model=df[['average_salary','Rating','type','size','industry','sector','company_revenue','Hourly',
    "Employer_Provided",'job_state','company_age','python_req', 'excel_req','r_req',
    'spark_req', 'aws_req','sql_req','scala_req', 'julia_req',
    'java_req', 'java2_req', 'tensor_req', 'seaborn_req', 'pandas_req',
    'tensor2_req','seniority','company_score']]

#get dummies
df_dum=pd.get_dummies(df_model)
#create train test split

X=df_dum.drop("average_salary",axis=1)
y=df_dum["average_salary"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#linear regression 
#linear regression using statsmodel

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

#linear regression using sklearn 

lm=LinearRegression()
lm.fit(X_train,y_train)
print(np.mean(cross_val_score(lm, X_train, y_train, cv=4,scoring = 'neg_mean_absolute_error')))


#Baseline lasso regression 

lasso_bl=Lasso(alpha=.13)
lasso_bl.fit(X_train,y_train)
print(np.mean(cross_val_score(lasso_bl, X_train, y_train, cv=4,scoring = 'neg_mean_absolute_error')))

#Gridsearch lasso regression

lml=Lasso()
parameters={"alpha" :np.arange(0.01,10,0.01)}
lasso_cv = GridSearchCV(lml,parameters,scoring='neg_mean_absolute_error',cv=3)
lasso_cv.fit(X_train,y_train)
lasso_cv.best_score_
lasso_cv.best_estimator_


#random forest 
rf=RandomForestRegressor()
rf.fit(X_train,y_train)
print(np.mean(cross_val_score(rf, X_train, y_train, cv=4,scoring = 'neg_mean_absolute_error')))

#hyper parameter tuning 
param_grid = {
    'n_estimators': [10, 100, 200],           # Number of trees in the forest
    'max_depth': [None, 10, 20, 30],         # Maximum depth of each tree
    'min_samples_split': [2, 5, 10],         # Minimum samples required to split
    'min_samples_leaf': [1, 2, 4],           # Minimum samples required at a leaf node
    'max_features': ['auto', 'sqrt', 'log2'], # Number of features to consider for split
    'bootstrap': [True, False],              # Whether to use bootstrap samples
    'random_state': [42],                    # Random seed for reproducibility
    'criterion': ['mse'],                    # Splitting criterion (Mean Squared Error)
    'oob_score': [True, False],              # Whether to use out-of-bag samples
    'warm_start': [False, True]}              # Reuse previous solution for incremental training


rf_cv=RandomForestRegressor()
rf_gs=RandomizedSearchCV(rf_cv,param_grid,scoring='neg_mean_absolute_error',n_jobs=-1,)
rf_gs.fit(X_train,y_train)

rf_gs.best_estimator_
rf_gs.best_score_
rf_gs.best_params_
#test ensembles 
y_pred_lm= lm.predict(X_test)
y_pred_lasso_bl=lasso_bl.predict(X_test)
y_pred_lasso_cv=lasso_cv.best_estimator_.predict(X_test)
y_pred_rf=rf.predict(X_test)
y_pred_rf_gs= rf_gs.predict(X_test)

mean_absolute_error(y_test,y_pred_lm)
mean_absolute_error(y_test,y_pred_lasso_bl)
mean_absolute_error(y_test,y_pred_lasso_cv)
mean_absolute_error(y_test,y_pred_rf)
mean_absolute_error(y_test,y_pred_rf_gs)


pickl = {'model': rf_gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

X_test.iloc[1,:]
model.predict(X_test.iloc[1,:].values.reshape(1,-1))

# Model
model = {"model_description": "Tuned Model: Random forest Grid Search ",
         "model_details": str(rf_gs.best_estimator_),
         "model_object": rf_gs.best_estimator_} 

with open(os.path.join(LOG_PATH, LOG_MODEL_PKL), "wb") as output_file:
    pickle.dump(model, output_file)
    
