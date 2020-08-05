import pandas as pd
from tox_block.prediction import make_predictions
import json

df = pd.read_csv("datasets/")

messages = []

for index, row in df.iterrows():
    messages.append(str(row[1]))


with open('results/', 'w') as file:
    file.write(json.dumps(make_predictions(messages, rescale=True)))
