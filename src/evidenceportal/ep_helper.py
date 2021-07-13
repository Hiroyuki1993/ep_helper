import pandas as pd
import requests
import json

class API:
    url = ""
    headers = {'Content-Type': 'application/json'}

    def __init__(self, url):
        self.url = url

    def prepost(self, df, col_pre, col_post):
        endpoint = self.url + "/prepost"
        payload = json.dumps({
            "data": df[["pre", "post"]].to_dict(orient="records"),
            "col_pre": col_pre,
            "col_post": col_post
        })
        response = requests.request("POST", endpoint, headers=self.headers, data=payload)
        return response.text

    def anova(self, df, col_group, col_y):
        endpoint = self.url + "/group"
        payload = json.dumps({
            "data": df[["group", "y"]].to_dict(orient="records"),
            "col_group": col_group,
            "col_y": col_y
        })
        response = requests.request("POST", endpoint, headers=self.headers, data=payload)
        return response.text
