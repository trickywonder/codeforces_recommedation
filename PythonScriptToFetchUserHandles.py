import requests
import pandas as pd
import numpy as np


def make_request(contest_id, user_handles):
    response = requests.get("https://codeforces.com/api/contest.ratingChanges?contestId="+str(contest_id))
    if response.status_code != 200:
        print("Something went wrong while making request")
    else:
        x = response.json()
        for entry in x["result"]:
            if entry["handle"] != "handles":
                user_handles.append(entry["handle"])
        user_handles = list(np.unique(user_handles))

def findUsersInTheSpecifiedContestIdRange(l, r):
    userHandleList = []
    for i in range(l, r+1):
        make_request(contest_id=i, user_handles=userHandleList)

    final_data = {"Handles": userHandleList}
    df = pd.DataFrame(final_data)
    df.to_csv("userHandles.csv")

findUsersInTheSpecifiedContestIdRange(594, 605)