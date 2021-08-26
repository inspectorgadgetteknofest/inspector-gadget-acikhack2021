# ZEROSHOT + BERT

Bu bölümde Zeroshot+BERT yapısını kullanarak oluşturduğumuz pipeline ile elinizdeki metinleri otomatik bir şekilde etiketlemeyi amaçladık. Verisetiniz belirlediğiniz sınıflarla eğitilmiş zeroshot ile tahminlenir. Belirlenen eşik değerin üzerindeki değerlerle oluşuturulan rafine veriseti ile BERT modeli eğitilir. Bu sayede etiketlenmemiş veri seti üzerinde en doğru tahmini yapabilen bir yapı oluşturulmuş olur.

#### Kaynak:Chalkidis, Ilias, et al. "An empirical study on large-scale multi-label text classification including few and zero-shot labels." arXiv preprint arXiv:2010.01653 (2020).

<p align="center">
  <img src="https://github.com/inspectorgadgetteknofest/inspector-gadget-acikhack2021/blob/main/Zeroshot/images/diagram.png">
</p>


## 1.1 Zeroshot:
Zeroshot modeli önce büyük bir külliyat ile  gözetimsiz öğrenme yöntemiyle eğitilir, cosine similarity ile dil yapısını ve kelimeler arasındaki anlamsal bağı öğrenmiş olur. Eğitilmiş model sonucunda verilen metni istenilen sınıflar arasında en uygun olanı ile eşleştirir.

#### Kaynak: https://joeddav.github.io/blog/2020/05/29/ZSL.html

#### ZEROSHOT Prediction:
```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model='joeddav/xlm-roberta-large-xnli')

sample_text = "Bugün hava çok yağmurlu. Yağmurlu havaları sevmem."

# Belirlenen sınıflar
candidate_labels = ["olumlu", "olumsuz"]

result = classifier(sample_text, candidate_labels)

print(result)
```

## 1.2 BERT:
Devlin vd. tarafından geliştirilen transformatörlerden çift yönlü kodlayıcı gösterimlere sahip olan BERT modeli ile birlikte, etiketlenmemiş metinlerin derin çift yönlü temsillerinin önceden eğitimi sırasında tüm katmanlarda sağ ve sol bağlam bilgilerinin dahil edilmesi sağlanmaktadır. Model, sonrasında ince ayar yapılarak göreve özgü şekilde eğitilebilmektedir. Bu görevler soru cevaplama, duygu analizi, metin sınıflandırma ve adlandırılmış varlık tanıma gibi farklı çeşitlerde olabilir.

#### Kaynak: https://arxiv.org/abs/2106.01735


#### BERT Finetuning:
```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(HUGGINGFACE_MODEL_PATH)
model = AutoModel.from_pretrained(HUGGINGFACE_MODEL_PATH)

from simpletransformers.classification import ClassificationModel

model_args = {
    "use_early_stopping": True,
    "early_stopping_delta": 0.01,
    "early_stopping_metric": "mcc",
    "early_stopping_metric_minimize": False,
    "early_stopping_patience": 5,
    "evaluate_during_training_steps": 6000,
    "fp16": False,
    "num_train_epochs":3  # Epoch sayısı
}

model = ClassificationModel(
    "bert", 
    HUGGINGFACE_MODEL_PATH,
     use_cuda=True, 
     args=model_args, 
     num_labels=7  # Sınıf sayısı
)

model.train_model(train, acc=sklearn.metrics.accuracy_score,output_dir=MODEL_OUTPUT_DIR)
```

#### BERT Prediction:
```python
# Tokenizerın içe aktarılması
tokenizer= AutoTokenizer.from_pretrained(tokenizer)

# Modelin içe aktarılması
model= AutoModelForSequenceClassification.from_pretrained(model)

# Pipelineın kurulması
nlp=pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

print(nlp(sample_text))
```

## 1.3 Eğitim ve test aşamasında kullanılan veri setleri ve sonuç değerleri:

  * <b> Turkish sentiment analysis:</b> <br>
  Veriseti içerisinde Pozitif, Negatif ve Nötr olmak üzere 3 sınıf barındırır. Bu görevde Pozitif ve Negatif etikeltli veriler ile işlem yapılmıştır. >=0.85 olacak şekilde eşik değer belirlenmiş ve elde edilen veriler ile BERT modeli eğitilmiştir. Eğitilen BERT modelinin test verisetindeki doğruluk değeri % 99, F1 Skoru %96 olarak hesaplanmıştır.
  
  * <b> ttc-4900 Multiclass Text Classification: </b> <a href= "https://www.kaggle.com/savasy/ttc4900">Link</a> <br>
  Kemik grup tarafından oluşturulan veri seti içerisinde "Siyaset", "Dünya" gibi 7 benzersiz sınıf ve 4539 satır veri barındırır. Bu veriseti kullanılarak yapılan Zeroshot prediction kısmında >=0.85 olacak şekilde eşik değer belirlenmiş ve elde edilne veriler ile BERT modeli eğitilmiştir. BERT modelinin test verisetindeki doğruluk değeri %94 olarak hesaplanmıştır.
  
  
