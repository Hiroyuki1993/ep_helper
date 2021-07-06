import pandas as pd
import requests
import json

class API:
    url = ""
    headers = {'Content-Type': 'application/json'}

    def __init__(self, url):
        self.url = url

    def prepost(self, df):
        endpoint = self.url + "/prepost"
        payload = json.dumps({
            "data": df[["pre", "post"]].to_json(orient="records")
        })
        response = requests.request("POST", endpoint, headers=self.headers, data=payload)
        return response.text

    def anova(self, df):
        endpoint = self.url + "/group"
        return "success"

    def clustering(self, df):
        endpoint = self.url + "/clustering"
        return "success"