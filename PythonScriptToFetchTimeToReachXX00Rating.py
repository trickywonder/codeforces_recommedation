import requests
import pandas as pd
import numpy as np
import csv
import time
import ast

def make_request(user_handle,contests_rating):
    refineResponse={}
    rate = ast.literal_eval(contests_rating)
    for x in rate:
        if(x['newRating']>=1920 and x['newRating']<2020):
            refineResponse['handle'] = user_handle
            refineResponse['time'] = x['ratingUpdateTimeSeconds']
            return refineResponse
            break
        if(x['newRating']>2100):
            break
    return 0


def read_csv(userFile):
    userHandleList = []
    with open(userFile) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line = 0
      for row in csv_reader:
        if(row[1]!="handle"):
          line+=1
          userRespose = make_request(row[1],row[2])
          if(userRespose!=0):
            userHandleList.append(userRespose)
          print(line)
          #time.sleep(0.03)
      df = pd.DataFrame(userHandleList)
      df.to_csv("userContestRatingUpto1800.csv")

read_csv("userContestRatingUpTo5000handles.csv")
