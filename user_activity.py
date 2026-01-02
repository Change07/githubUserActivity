import requests
import pandas as pd

def main(username):
    # get user activity
    api_uri = f"https://api.github.com/users/{username}/events/public"

    headers = {"username" : f"{username}"}

    response = requests.get(api_uri, headers=headers).json()

    print(response)

    dataFrame = pd.DataFrame(response)
    # print(dataFrame)
    # print(dataFrame.values[0][3]["name"])
    # display user activity 

if __name__ == "__main__":
    main("Change")
