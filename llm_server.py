# coding = utf-8
import os
import re
from tqdm import tqdm
import requests
import json
import time


class ModelAPI():
    def __init__(self, MODEL_URL):
        self.url = MODEL_URL
        return

    def send_request(self, message, history):
        data = json.dumps({"message":message, "history":history})
        headers = {'Content-Type': 'application/json'}
        try:
            res = requests.post(self.url, data=data, headers=headers)
            print(res)
            predict = json.loads(res.text)["output"][0]
            history = json.loads(res.text)["history"]
            return predict, history
        except Exception as e:
            print("request error", e)
            return "", []

    def chat(self, query, history=[]):
        message = [{"role": "user", "content": query}]
        count = 0
        response = ''
        history = []
        while count <=10:
            try:
                count +=1
                response, history = self.send_request(message, history)
                if response:
                    return response, history
            except Exception as e:
                print('Exception:', e)
                time.sleep(1)
        return response, history
