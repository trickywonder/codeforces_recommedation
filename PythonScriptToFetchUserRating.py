import requests
import pandas as pd
import numpy as np
import csv

def make_request(user_name):
    refineResponse={}
    refineResponse["handle"]=user_name
    allCon=[]
    response = requests.get("https://codeforces.com/api/user.rating?handle="+str(user_name))
    if response.status_code != 200:
        print("Something went wrong while making request")
    else:
        x = response.json()
        for oneContest in x["result"]:
              oneC={}
              oneC["ratingUpdateTimeSeconds"]=oneContest["ratingUpdateTimeSeconds"]
              oneC["oldRating"]=oneContest["oldRating"]
              oneC["newRating"]=oneContest["newRating"]
              allCon.append(oneC)
        refineResponse["rating"]=allCon
    return refineResponse


def read_csv(userFile):
    userHandleList = []
    with open(userFile) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if(row[1]!="Handles"):
          userRespose = make_request(row[1])
          userHandleList.append(userRespose)
          print(userRespose)
        line_count+=1
        if(line_count==5):
          break
        df = pd.DataFrame(userHandleList)
        df.to_csv("userContestRating.csv")

read_csv("userHandles.csv")
