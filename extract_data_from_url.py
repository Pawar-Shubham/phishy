import pandas as pd
import tldextract as td
import urllib as ub
import numpy as np
#extract_data_from_url.py is a python file which is used to extract specific data from the url to be further used to predict


class url_extractor:
    data = [] #this list will hold all the data needed to predict
    ch_repeated = [] #this holds the letters and numbers repeated in the url
    domain_repeated = [] #this list holds the letters and numbers repeated in the domain name
    subdomain_repeated = [] #this list holds the letters and numbers repeated in the subdomain
    
    def __init__(self,url): #initiailizing the variables needed
        self.domain = ub.parse.urlparse(url).netloc #extracting domain name from the url
        self.path = ub.parse.urlparse(url).path #extracting path from the url 
        self.query = ub.parse.urlparse(url).query #extracting query from the url
        self.fragment = ub.parse.urlparse(url).fragment #extracting fragments from the url
        self.subdomain = td.extract(url).subdomain #extracting subdomain from the url
        self.repeated(url,self.domain,self.subdomain) #method called to get all the repeated characters and numbers from the url,domain and subdomain
        self.extract_data(url) #method call to extract specific data needed
    
    def is_SC(self,url):    #method to record all the special characters in the url, domain and subdomain
        SC = []
        special_characters = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","]","}","|",'\\',":",";","'","'","<",',',">",".","?","/"]
        for i in special_characters:
            if i in url:
                SC.append(i)
        return(SC)
           
    def repeated(self,url,domain,subdomain): #method to record all the repeated characters in the url, domain and subdomain
        #extracting repeated elements from url
        for i in url:
            if url.count(i) > 1:
                if i not in self.ch_repeated:
                    self.ch_repeated.append(i)
        #extracting repeated elements from domain
        for i in domain:
            if domain.count(i) > 1:
                if i not in self.domain_repeated:
                    self.domain_repeated.append(i)
        #extracting repeated elements from subdomain
        if len(subdomain)>0:
            for i in subdomain:
                if subdomain.count(i) > 1:
                    if i not in self.subdomain_repeated:
                        self.subdomain_repeated.append(i)
   
    #method to get the number of digits from the url 
    def n_Digits(self,url):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        n_Digits = []
        for i in numbers:
            if i in url:
                n_Digits.append(i)
        return(n_Digits)
    
    #method to extract the repeated digits from the Subdomain
    def repeated_n_Digits_SubDomain(self):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        repeated_n_Digits = []
        for i in numbers:
            if i in self.subdomain_repeated:
                repeated_n_Digits.append(i)
        return(repeated_n_Digits)
    
    #method to extract the repeated digits from the Domain
    def repeated_n_Digits_Domain(self):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        repeated_n_Digits = []
        for i in numbers:
            if i in self.domain_repeated:
                repeated_n_Digits.append(i)
        return(repeated_n_Digits)
    
    #method to extract the repeated digits from the url
    def repeated_n_Digits(self,url):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        repeated_n_Digits = []
        for i in numbers:
            if i in self.ch_repeated:
                repeated_n_Digits.append(i)
        return(repeated_n_Digits)
    
    #main method to extract all the data we need to predict whether the url is phishy or not
    def extract_data(self,url):
        url_length = len(url) 
        number_of_dots_in_url = url.count('.')
        having_repeated_digits_in_url = 1 if len(self.repeated_n_Digits(url))>0 else 0
        number_of_digits_in_url = len(self.n_Digits(url))
        number_of_special_char_in_url = len(self.is_SC(url))
        number_of_hyphens_in_url = url.count('-')
        number_of_underline_in_url = url.count('_')
        number_of_slash_in_url = url.count('/')
        number_of_questionmark_in_url = url.count('?')
        number_of_equal_in_url = url.count('=')
        number_of_at_in_url = url.count('@')
        number_of_dollar_in_url = url.count('$')
        number_of_exclamation_in_url = url.count('!')
        number_of_hashtag_in_url = url.count('#')
        number_of_percent_in_url = url.count('%')
        domain_length = len(self.domain)
        number_of_dots_in_domain = self.domain.count('.')
        number_of_hyphens_in_domain = self.domain.count('-')
        having_special_characters_in_domain = 1 if len(self.is_SC(self.domain))>0 else 0 
        number_of_special_characters_in_domain = len(self.is_SC(self.domain))
        having_digits_in_domain = 1 if len(self.n_Digits(self.domain))>0 else 0
        number_of_digits_in_domain = len(self.n_Digits(self.domain))
        having_repeated_digits_in_domain = 1 if len(self.repeated_n_Digits_Domain())>0 else 0
        number_of_subdomains = self.subdomain.count('.') + 1 if len(self.subdomain)>0 else 0 
        having_dot_in_subdomain = 1 if self.subdomain.count('.')>0 else 0
        having_hyphen_in_subdomain = self.subdomain.count('-')
        average_subdomain_length = len(self.subdomain)/number_of_subdomains if number_of_subdomains>0 else 0
        having_special_characters_in_subdomain = 1 if len(self.is_SC(self.subdomain))>0 else 0
        number_of_special_characters_in_subdomain = len(self.is_SC(self.subdomain))
        having_digits_in_subdomain = 1 if len(self.n_Digits(self.subdomain))>0 else 0
        number_of_digits_in_subdomain = len(self.n_Digits(self.subdomain))
        having_repeated_digits_in_subdomain = 1 if len(self.repeated_n_Digits_SubDomain())>0 else 0
        having_path = 1 if len(self.path)>0 else 0
        path_length  = len(self.path)
        having_query = 1 if len(self.query)>0 else 0 
        having_fragment = 1 if len(self.fragment)>0 else 0
        
        #storing all the extracted data and then returning it 
        self.data = [url_length,
        number_of_dots_in_url,
        having_repeated_digits_in_url,
        number_of_digits_in_url,
        number_of_special_char_in_url,
        number_of_hyphens_in_url,
        number_of_underline_in_url,
        number_of_slash_in_url,
        number_of_questionmark_in_url,
        number_of_equal_in_url,
        number_of_at_in_url,
        number_of_dollar_in_url,
        number_of_exclamation_in_url,
        number_of_hashtag_in_url,
        number_of_percent_in_url,
        domain_length,
        number_of_dots_in_domain,
        number_of_hyphens_in_domain,
        having_special_characters_in_domain,
        number_of_special_characters_in_domain,
        having_digits_in_domain,
        number_of_digits_in_domain,
        having_repeated_digits_in_domain,
        number_of_subdomains,
        having_dot_in_subdomain,
        having_hyphen_in_subdomain,
        average_subdomain_length,
        having_special_characters_in_subdomain,
        number_of_special_characters_in_subdomain,
        having_digits_in_subdomain,
        number_of_digits_in_subdomain,
        having_repeated_digits_in_subdomain,
        having_path,
        path_length,
        having_query,
        having_fragment]
    #method used to return extracted data from the url
    def get_data(self):
        return self.data
