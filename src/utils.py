import os
import sys

import numpy as np
import pandas as pd
import dill 
import pickle
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    report = {}
    try:
    
        for i, (model_name,model) in enumerate(models.items()):
            param_grid = params[model_name]

            gsv = GridSearchCV(estimator=model,param_grid=param_grid,n_jobs=-1)
            gsv.fit(X_train,y_train)
            model.set_params(**gsv.best_params_)
            model.fit(X_train,y_train) 
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test,y_pred)
            report[model_name] = r2

        return report

    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return(dill.load(file_obj))
    except Exception as e:
        raise CustomException(e,sys)