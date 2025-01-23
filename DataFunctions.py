#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder


class data_understanding:
    def __init__(self, file):
        """
        Initializes the data understanding class
        """
        self.data = self.load_data(file)
        

    def load_data(self, file):
        """
        Loading the csv file
        """
        return pd.read_csv(file, encoding = "latin-1")
    
    def first_rows(self):
        """
        Checks the first 5 rows of the dataset
        """
        return self.data.head()
    
    def last_rows(self):
        """
        Checks the last 5 rows of the dataset
        """
        return self.data.tail()
     
    def data_shape(self):
        """
        Returns the shape of the dataset
        """
        return self.data.shape
        
    def data_info(self):
        """
        Returns the information about the dataset.
        """
        return self.data.info()

    def data_description(self):
        """
        Returns the description of the dataset
        """
        return self.data.describe()
    
    def check_missing_data_and_duplicates(self):
        """
        Summarizes a pandas DataFrame by displaying whether it's missing values or has duplicates.
        
        Returns:
            None: Prints the dataset description.
        """
        print("---------------------Missing Values-----------------")
        print(self.data.isnull().sum())  # Missing values per column

        print("\n\n ----------------Duplicates---------------------")
        print(self.data.duplicated(keep=False).sum())  # Duplicates in the DataFrame
    

# In[ ]:



