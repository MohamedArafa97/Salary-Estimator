# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:40:37 2023

@author: Mohamed Arafa
"""
DATAPATH=r"C:\Users\Mohamed Arafa\Salary_Estimator\data\raw"
PROCESSEDPATH=r"C:\Users\Mohamed Arafa\Salary_Estimator\data\processed"

import pandas as pd
import os 


raw_df = pd.read_csv(os.path.join(DATAPATH,"glassdoor_jobs.csv"))

#Job title standarization
#size grouping 
#salary estimate parsing

df=raw_df.copy()

df=df[df["Salary Estimate"]!="-1"]

salary=df["Salary Estimate"].copy()

for x in salary.index :
    
   parts = salary[x].split("(")
  
   
   if len(parts)>1 :
       
       salary[x]=parts[0]
       
for x in salary.index :
     
    salary[x] = salary[x].replace("$","")
    salary[x]= salary[x].replace("K","")
    salary[x]= salary[x].lower().replace("per hour","")
    salary[x]= salary[x].lower().replace("employer provided salary:","")
    
    
df["Hourly"]=0
df["Employer_Provided"]=0

for i  in range(len(df)) :
    
    if 'per hour' in df['Salary Estimate'].iloc[i].lower() :
        
        df["Hourly"].iloc[i]=1
        
    if 'employer provided' in df['Salary Estimate'].iloc[i].lower() :
        
        df["Employer_Provided"].iloc[i]=1
                
  
df["min_salary"]=[float(salary.iloc[i].split("-")[0]) if len(salary.iloc[i].split("-")) >1 else float(salary.iloc[i]) for i in range(len(salary)) ]          
df["max_salary"]=[float(salary.iloc[i].split("-")[1]) if len(salary.iloc[i].split("-")) >1 else float(salary.iloc[i]) for i in range(len(salary)) ]          
df["average_salary"]=(df["min_salary"]+df["max_salary"])/2
df.dtypes           

#company name text only 

df["company_txt"]= df.apply(lambda x: x["Company Name"] if x["Rating"] < 0 else x["Company Name"][ : -3] , axis = 1)


#state code only 

df["job_state"]=df["Location"].apply(lambda x : x.split(",")[1] if len(x.split(",")) > 1 else x )

df["job_state"].value_counts()

# company age

df["company_age"]=df["founded"].apply(lambda x : x if x<1 else 2023-x)


#cleaning job description getting tech requirements 

#python
df["python_req"]=[1 if "python" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

#excel
df["excel_req"]=[1 if "excel" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["spark_req"]=[1 if "spark" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["aws_req"]=[1 if "aws" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["sql_req"]=[1 if "sql" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["r_req"]=[1 if "rstudio" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["scala_req"]=[1 if "scala" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["julia_req"]=[1 if "julia" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["java_req"]=[1 if "javascript" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["java2_req"]=[1 if "java script" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["tensor_req"]=[1 if "tensor" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["tensor2_req"]=[1 if "tensorflow" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["seaborn_req"]=[1 if "seaborn" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]

df["pandas_req"]=[1 if "pandas" in df["Job Description"].iloc[i].lower() else 0 for i in range(len(df))]



## Job title and seniority 

def title_simplifier(title):
    if 'data scientist' in title.lower() or "data science" in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst'  in title.lower()  or "data analyst" in title.lower():
        return 'data analyst'
    elif 'machine learning' in title.lower()  or "ML engineer" in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower()\
    or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower() or 'junior' in title.lower()or 'entry level' in title.lower() :
        return 'jr'
    else:
        return 'na'
    
  
df["jobtitle_simp"]=df["Job Title"].apply(title_simplifier)
df["jobtitle_simp"].value_counts()
df["seniority"]=df["Job Title"].apply(seniority)
df["seniority"].value_counts()



##  Fix states names 

df.job_state.value_counts()

for i in range(len(df)) :
    if  "united states" in df["job_state"].iloc[i].lower() :
        df["job_state"].iloc[i] = "USA"
    elif "california" in df["job_state"].iloc[i].lower():
        df["job_state"].iloc[i] = "CA"
    elif "oregon" in df["job_state"].iloc[i].lower():
        df["job_state"].iloc[i] = "OR"
    elif "texas" in df["job_state"].iloc[i].lower():
        df["job_state"].iloc[i] = "TX"
    elif "new york" in df["job_state"].iloc[i].lower():
        df["job_state"].iloc[i] = "NY"
    elif "alabama" in df["job_state"].iloc[i].lower():
        df["job_state"].iloc[i] = "AL"
    elif "Illinois" in df["job_state"].iloc[i].lower():
         df["job_state"].iloc[i] = "IL"

df["job_state"].replace(" CA", "CA", inplace=True)
df.job_state.value_counts()



df["jobdesc_length"] = [len(df["Job Description"].iloc[i]) for i in range(len(df))]
df.jobdesc_length

df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.Hourly ==1 else x.min_salary, axis =1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.Hourly ==1 else x.max_salary, axis =1)
df['average_salary'] = df.apply(lambda x: x.average_salary*2 if x.Hourly ==1 else x.max_salary, axis =1)

df[df["Hourly"]==1][["min_salary","max_salary","average_salary"]]

df.company_txt= [ df.company_txt.iloc[i].replace("\n","") for i in range(len(df))]

df.company_txt

    
processed_df=df.copy()

processed_df.to_csv(os.path.join(PROCESSEDPATH,"processed_df.csv"),index=False)

test_df=pd.read_csv("processed_df.csv")

