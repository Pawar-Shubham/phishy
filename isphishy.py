import pandas as pd
import tldextract as td
import urllib as ub
import numpy as np
import pickle
from extract_data_from_url import url_extractor


class isPhishy():
    def __init__(self):
        self.model = pickle.load(open('model','rb')) #importing the model we created in model.py
        
    def checkURL(self,url):
        urlextractor = url_extractor(url) #importing url_extractor from the extract_data_from_url.py to extract url data
        url_data = np.array(urlextractor.get_data()).reshape(1,-1) #changing the shape of array to 2d as model take 2d array as input
        result = self.model.predict(url_data) #predicting whether the url is phishy or not
        #if the url is phishy the model will return 1 and 0 for legit
        isPhishy = False if result[0] == 0 else True #converting 1 and 0 into boolean, 1,True for phishy website amd 0,False for legit site.
        return isPhishy #returning the boolean variable

#taking the url as input from the user through the terminal
url = input("Paste the url to see whether the site is a phishing site or not :- \n")
ip = isPhishy() #creating the instance  
result = ip.checkURL(url) #calling the method to check whether the url is phishy
if result:
    print("This website is phishy")
elif not result:
    print("This website is legit")