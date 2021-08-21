import pandas as pd
from transformers import pipeline
from tqdm import tqdm


data = pd.read_excel("data.xlsx")


classifier = pipeline("zero-shot-classification", model='joeddav/xlm-roberta-large-xnli')


candidate_labels = ["olumlu", "olumsuz"]


text_list, olumlu_score_list, olumsuz_score_list, real_class = [], [], [], []


for i in tqdm(range(len(data))):

    
  result = classifier(data["text"][i], candidate_labels)
  text_list.append(data["text"][i])
  olumlu_score_list.append(result['scores'][result["labels"].index('olumlu')])
  olumsuz_score_list.append(result['scores'][result["labels"].index('olumsuz')])
  real_class.append(data["duygu"][i])



labels = pd.DataFrame()
labels["text"] = data["text"]
labels['olumlu_score'] = olumlu_score_list
labels['olumsuz_score'] = olumsuz_score_list
labels["real_class"] = real_class

labels.to_excel("result.xlsx")
