"""
Created on Fri Nov 16 13:38:26 2018
@author: Shyam Sunder Kumar

Task : Extract data from Json file to make Pandas Dataframe

"""

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json

# Input data files are available in the "../input/" directory.
# Extract data from Json file
    
data = []
with open('../input/News_Category_Dataset.json') as f:
    for line in f:
        data.append(json.loads(line))

news_data = pd.DataFrame.from_dict(data) # Make pandas dataframe

# Dump to a csv file

news_data.to_csv("../cleaned/newsdata.csv",index = False)
