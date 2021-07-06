import pandas as pd
import requests
import json

class API:
    url = ""
    def __init__(self, url):
        self.url = url

    def prepost(self, df):
        endpoint = self.url + "/prepost"
        return "success"

    def anova(self, df):
        endpoint = self.url + "/group"
        return "success"

    def clustering(self, df):
        endpoint = self.url + "/clustering"
        return "success"