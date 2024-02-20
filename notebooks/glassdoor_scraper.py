# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:32:36 2020

author: Kenarapfaik
url: https://github.com/arapfaik/scraping-glassdoor-selenium
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import requests


def get_jobs(keyword, num_jobs, verbose, slp_time):
    
    
   try:
       
       '''Gathers jobs as a dataframe, scraped from Glassdoor'''
       
       #Initializing the webdriver
       options = webdriver.ChromeOptions()
       driver = webdriver.Chrome()
       driver.set_window_size(1120, 1000)
       
       url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
       #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
       driver.get(url)
       jobs = []
       page_num=1

       while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

           time.sleep(slp_time)
         
           
           try:    
            driver.find_element(By.XPATH,"""//*[@id="LoginModal"]/div/div/div/div[2]/button""").click()  #clicking to the X.
           except NoSuchElementException:
            pass 
           
           #Going through each job in this page
           
          
           job_buttons = driver.find_elements(By.XPATH,"//li[contains(@class,'react-job-listing')]")           #jl for Job Listing. These are the buttons we're going to click.
           
           for job_button in job_buttons:  

               print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
               
               if len(jobs) >= num_jobs:
                   break

               job_button.click() 
               time.sleep(5)
               try:    
                   driver.find_element(By.XPATH,"""//*[@id="LoginModal"]/div/div/div/div[2]/button""").click()  #clicking to the X.
               except NoSuchElementException:
                    pass 
               time.sleep(2)
               try:  
                       job_description = driver.find_element(By.XPATH,"//button[text()='Retry your search']").click()
               except NoSuchElementException:
                       pass 
               time.sleep(2)
              
               try:    
                   driver.find_element(By.XPATH,"""//*[@id="LoginModal"]/div/div/div/div[2]/button""").click()  #clicking to the X.
               except NoSuchElementException:
                    pass 
               time.sleep(2)
               collected_successfully = False
               
               while not collected_successfully:
                   try:
                       company_name = driver.find_element(By.XPATH,"""//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div""").text
                       location = driver.find_element(By.XPATH,"""//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]""").text
                       job_title = driver.find_element(By.XPATH,"""//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]""").text
                       collected_successfully = True
                   except:
                       company_name=-1
                       location=-1
                       job_title=-1
                       time.sleep(5)
                       
               try:    
                   driver.find_element(By.XPATH,"""//*[@id="JobDescriptionContainer"]/div[2]""").click()  #clicking to the X.
               except NoSuchElementException:
                    pass 
                
                   
               try:  
                       job_description = driver.find_element(By.XPATH,"//div[@class='jobDescriptionContent desc']").text
               except NoSuchElementException:
                       job_description = -1 #You need to set a "not found value. It's important."

               try:
                   salary_estimate = driver.find_element(By.XPATH,"""//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span""").text
               except NoSuchElementException:
                   salary_estimate = -1 #You need to set a "not found value. It's important."
               
               try:
                   rating = driver.find_element(By.XPATH,"""//*[@id="employerStats"]/div[1]/div[1]""").text
               except NoSuchElementException:
                   rating = -1 #You need to set a "not found value. It's important."
                   
               try:  
                   size = driver.find_element(By.XPATH,"//span[text()='Size']//following-sibling::span[1]").text
               except NoSuchElementException:
                   size = -1 #You need to set a "not found value. It's important."
                   
               try:  
                    founded = driver.find_element(By.XPATH,"//span[text()='Founded']//following-sibling::span[1]").text
               except NoSuchElementException:
                    founded = -1 #You need to set a "not found value. It's important."
                    
               try:  
                    type = driver.find_element(By.XPATH,"//span[text()='Type']//following-sibling::span[1]").text
               except NoSuchElementException:
                    type = -1 #You need to set a "not found value. It's important."
                    
               try:  
                    industry = driver.find_element(By.XPATH,"//span[text()='Industry']//following-sibling::span[1]").text
               except NoSuchElementException:
                    industry = -1 #You need to set a "not found value. It's important."
                    
               try:  
                    sector = driver.find_element(By.XPATH,"//span[text()='Sector']//following-sibling::span[1]").text
               except NoSuchElementException:
                    sector = -1 #You need to set a "not found value. It's important."
                    
               try:  
                     company_revenue = driver.find_element(By.XPATH,"//span[text()='Revenue']//following-sibling::span[1]").text
               except NoSuchElementException:
                     company_revenue = -1 #You need to set a "not found value. It's important."
                     
               try:  
                      career_opportunities = driver.find_element(By.XPATH,"//span[text()='Career Opportunities']//following-sibling::span[2]").text
               except NoSuchElementException:
                      career_opportunities = -1 #You need to set a "not found value. It's important."
               try:  
                      comp_benefits = driver.find_element(By.XPATH,"//span[text()='Comp & Benefits']//following-sibling::span[2]").text
               except NoSuchElementException:
                      comp_benefits = -1 #You need to set a "not found value. It's important."
               try:  
                      culture_values = driver.find_element(By.XPATH,"//span[text()='Culture & Values']//following-sibling::span[2]").text
               except NoSuchElementException:
                      culture_values = -1 #You need to set a "not found value. It's important."
                      
               try:  
                      senior_management = driver.find_element(By.XPATH,"//span[text()='Senior Management']//following-sibling::span[2]").text
               except NoSuchElementException:
                      senior_management = -1 #You need to set a "not found value. It's important."
                      
               try:  
                      work_life_balance = driver.find_element(By.XPATH,"//span[text()='Work/Life Balance']//following-sibling::span[2]").text
               except NoSuchElementException:
                      work_life_balance = -1 #You need to set a "not found value. It's important."
                    
               #Printing for debugging
               if verbose:
                   print("Job Title: {}".format(job_title))
                   print("Salary Estimate: {}".format(salary_estimate))
                   print("Job Description: {}".format(job_description[:500]))
                   print("Rating: {}".format(rating))
                   print("Company Name: {}".format(company_name))
                   print("Location: {}".format(location))
                   print("founded: {}".format(size))
                   print("size: {}".format(founded))
                   print("type: {}".format(type))
                   print("industry: {}".format(industry))
                   print("sector: {}".format(sector))
                   print("company_revenue: {}".format(company_revenue))
                   print("career_opportunities: {}".format(career_opportunities))
                   print("benefits: {}".format(comp_benefits))
                   print("culture_values: {}".format(culture_values))
                   print("senior_management: {}".format(senior_management))
                   print("work_life_balance: {}".format(work_life_balance))
                  
               jobs.append({"Job Title" : job_title,
               "Salary Estimate" : salary_estimate,
               "Job Description" : job_description,
               "Rating" : rating,
               "Company Name" : company_name,
               "Location" : location,
               "size" : size , 
               "type" : type , 
               "founded" : founded ,
               "industry" : industry 
               ,"sector" : sector,
               "company_revenue": company_revenue,
               "career_opportunities" : career_opportunities,
               "benefits":comp_benefits,
               "culture_values":culture_values,
               "senior_management":senior_management,
               "work_life_balance":work_life_balance})
               
          # Clicking on the "next page" button
           try:
             print("Page {} scrapped successfully ".format(page_num))  
             page_num += 1  
             print("Next page")
             driver.find_element(By.XPATH,"""//*[@id="MainCol"]/div[2]/div/div[1]/button[7]""").click()
             print("Page {} ".format(page_num)) 
           except NoSuchElementException:
                 print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
                 break
             
           time.sleep(5)

           try:    
              driver.find_element(By.XPATH,"""//*[@id="LoginModal"]/div/div/div/div[2]/button""").click()  #clicking to the X.
           except NoSuchElementException:
              pass 
                
       return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
       
   except Exception as e:
        # Handle the exception (e.g., log it or print an error message)
        print(f"An error occurred: {str(e)}")
        print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
        print("Number of pages scrapped : {} ".format(page_num))
        return pd.DataFrame(jobs)
        
        