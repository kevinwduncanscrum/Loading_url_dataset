#Loading_url_dataset

#load dataset from our scikit learn toy dataset module
from sklearn import datasets

#having loaded the dataset, we may explore its properties to get an idea of its features 
#and how the data is stored. For example, we can use the DESCR property to get a 
#general description of the dataset. 

datastes DESCR
iris = datasets.load_iris()

#import the pandas library
import pandas as pd

#import the urllib module for python 3, 
#which provides a high-level interface for retrieving files across the World Wide Web
import urllib3


urlRequest = urllib.request.Request(myUrl)
#specify the URL string and store it in a local object
myUrl = "http://aima.cs.berkeley.edu/data/iris.csv"

#make a request by passing our URL string as a parameter 
#into the request class constructor of the urllib request module
urlRequest = urllib3.request.Request(myUrl)

#Got this error: AttributeError: 'module' object has no attribute 'request'