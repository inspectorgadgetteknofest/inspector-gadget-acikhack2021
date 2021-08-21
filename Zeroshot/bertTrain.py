# Kütüphanelerin import edilmesi

!pip install simpletransformers
!pip install transformers
!pip install progress

import pandas as pd
import re
from sklearn.model_selection import train_test_split
import sklearn
import os
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setinin okunması

data = pd.read_excel("zeroshot_data.xlsx")


# Veri setinin düzenlenmesi

# Sınıf etiketlerinin metinden sayıya dönüştürülmesi


from sklearn.preprocessing import LabelEncoder

labels = list(set(list(data["predicted_class"])))


le = LabelEncoder()
le.fit(labels)
data["predicted_class"] = le.transform(data["predicted_class"])


# NaN değerlerin atılması

data.dropna(axis= 0, inplace=True)



# Indexin resetlenmesi

data = data.reset_index(drop = True)

# CleanText fonksiyonunun tanımlanması ve uygulanması

def cleanText(input_sentence):
 
  tmp= [word.replace('A','a') for word in input_sentence.split(' ')]
  tmp= [word.lower() for word in tmp]
  tmp= [word.replace('i̇','i') for word in tmp]
  tmp = [re.sub('[^A-Za-z0-9ğüşıçöiâî]+', ' ', word) for word in tmp]
  tmp = [word.strip(' ') for word in tmp]
  tmp1 =' '.join(tmp)

  return tmp1

data["text"] = data["text"].apply(cleanText)


# Train/Test split


X_train, X_test, y_train, y_test = train_test_split(data["text"],data["predicted_class"], test_size= .3, stratify=data['predicted_class'], random_state = 42)



train = pd.concat([X_train,y_train], axis = 1)

test = pd.concat([X_test,y_test], axis = 1)



# Transformers

HUGGINGFACE_MODEL_PATH = "loodos/bert-base-turkish-cased"
MODEL_OUTPUT_DIR = 'output'

from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(HUGGINGFACE_MODEL_PATH)
model = AutoModel.from_pretrained(HUGGINGFACE_MODEL_PATH)

from simpletransformers.classification import ClassificationModel


# Train

model_args = {
    "use_early_stopping": True,
    "early_stopping_delta": 0.01,
    "early_stopping_metric": "mcc",
    "early_stopping_metric_minimize": False,
    "early_stopping_patience": 5,
    "evaluate_during_training_steps": 6000,
    "fp16": False,
    "num_train_epochs":5
}

model = ClassificationModel(
    "bert", 
    HUGGINGFACE_MODEL_PATH,
     use_cuda=True, 
     args=model_args, 
     num_labels=7
)

model.train_model(train, acc=sklearn.metrics.accuracy_score,output_dir=MODEL_OUTPUT_DIR)


# Kaydedilmiş epoch dosyalarının pathlerinin alınması

EPOCH_PATH = [MODEL_OUTPUT_DIR +"/"+ i for i in os.listdir(MODEL_OUTPUT_DIR) if "epoch" in i]




from tqdm.notebook import tqdm



from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer, AutoModelForSequenceClassification


def get_model(path):
  result = {}
  plt.rcParams["figure.figsize"] = (20,10)
  for epoch in path:

    tokenizer= AutoTokenizer.from_pretrained(epoch)

    # build and load model, it take time depending on your internet connection
    model= AutoModelForSequenceClassification.from_pretrained(epoch)

    # make pipeline
    nlp=pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


    pred_label_list, true_label_list = [],[]
    cou = 0
    max = len(test["text"])
    
    for t,l,i in zip(test["text"], test["predicted_class"], tqdm(range(max))):

      cou+=1
      true_label_list.append(l)
      pred_label_list.append(int(nlp(t)[0]["label"].lstrip("LABEL_")))

    df = pd.DataFrame()
    df["true"] = true_label_list
    df["pred"] = pred_label_list
    print(df)


    acc = accuracy_score(df["true"], df["pred"])
    result[f"{EPOCH_PATH.index(epoch)+1}. epoch Accuracy"] = acc
    print(acc)
    print(classification_report(df["true"], df["pred"]))

    sns.heatmap(confusion_matrix(df["true"], df["pred"]), annot = True, fmt = "g")
    plt.show()





get_model(EPOCH_PATH)

# train


from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer, AutoModelForSequenceClassification
def get_model(path):
  result = {}
  plt.rcParams["figure.figsize"] = (20,10)
  for epoch in path:

    tokenizer= AutoTokenizer.from_pretrained(epoch)

    # build and load model, it take time depending on your internet connection
    model= AutoModelForSequenceClassification.from_pretrained(epoch)

    # make pipeline
    nlp=pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


    


    pred_label_list, true_label_list = [],[]
    cou = 0
    max = len(test["text"])
    for t,l, i in zip(train["text"], train["predicted_class"], tqdm(range(max))):
      cou+=1
      true_label_list.append(l)
      pred_label_list.append(int(nlp(t)[0]["label"].lstrip("LABEL_")))

    df = pd.DataFrame()
    df["true"] = true_label_list
    df["pred"] = pred_label_list
    print(df)


    acc = accuracy_score(df["true"], df["pred"])
    result[f"{EPOCH_PATH.index(epoch)+1}. epoch Accuracy"] = acc
    print(acc)
    print(classification_report(df["true"], df["pred"]))

    sns.heatmap(confusion_matrix(df["true"], df["pred"]), annot = True, fmt = "g")
    plt.show()

get_model(EPOCH_PATH)

