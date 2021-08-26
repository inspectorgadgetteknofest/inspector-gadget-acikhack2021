from flask import Flask, redirect, url_for, render_template, request, flash
from tqdm import tqdm
from simpletransformers.classification import ClassificationModel
from sklearn.metrics import accuracy_score


class Zeroshot:

	def __init__(self):
		self.model_path = "joeddav/xlm-roberta-large-xnli"
	
	def get_model(self):
		"""
		Zero-shot modelini getirir.
		"""
		
		from transformers import pipeline
		self.classifier = pipeline("zero-shot-classification", model=self.model_path)

		
	def predict(self, data, candidate_labels, THRESHOLD_PARAM = .85):
		
		"""
		Zero-shot modeli ile verilen metni verilen etiketler arasından en yakınıyla eşleştirir.

		Input:
			data [list<str>]: Zeroshot ile tahmin ettirilecek metin verisi.
			
			candidate_labels [list<str>]: Tahmin yapılırken kullanılacak sınıflar.
			
			THRESHOLD_PARAM [float]: Modelin doğruluğunu arttırmak için kullandığımız eşik değer parametresi
		"""
		predicted_class_list = []
		self.get_model()
		
		for idx in tqdm(range(len(data))):
			
			result = self.classifier(data[idx], candidate_labels)
			
			
			if result["scores"][0] >= THRESHOLD_PARAM:
				
				predicted_class_list.append(result["labels"][0])
				
			else: predicted_class_list.append("-")

		return predicted_class_list
				
class Bert:
	
	def __init__(self):
		
		self.path = "loodos/bert-base-turkish-cased"
		
	
	def get_model(self, path):
		
		"""
		Kullanılacak BERT modelini getiren fonksiyon
		
		Input:
			path [str]: huggingface'teki model adresi (Örnek: loodos/bert-base-turkish-cased)
		"""
		
		from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer, AutoModelForSequenceClassification

		tokenizer = AutoTokenizer.from_pretrained(self.path)

	
		model = AutoModelForSequenceClassification.from_pretrained(self.path)

		
		self.nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
		
		
	
	def train(self, train_dataset, num_labels, output_dir):
		
		"""
		BERT ince ayarı için kullanılan fonksiyon.
		
		Input:
			train_dataset [DataFrame]: text ve label olacak şekilde eğitim veriseti
			
			num_labels [int]: sınıf sayısı
			
			output_dir [str]: model eğitimi sonlandıktan sonra model dosyasının kaydedileceği adres
			
			
		"""
		
		model_args = {
			"use_early_stopping": True,
			"early_stopping_delta": 0.01,
			"early_stopping_metric": "mcc",
			"early_stopping_metric_minimize": False,
			"early_stopping_patience": 5,
			"evaluate_during_training_steps": 6000,
			"fp16": False,
			"num_train_epochs": 3
		}

		model = ClassificationModel(
			"bert", 
			self.path,
			use_cuda=True, 
			args=model_args, 
			num_labels=num_labels
		)

		model.train_model(train_dataset, acc=accuracy_score, output_dir=output_dir)
	
	def predict(self, predict_text, model_path):
		
		"""
		İnce ayar yapılan BERT modeliyle tahminleme yapan fonksiyon

		Returns:
			predict_text [list<str>]: Tahmin edilecek metin
			
			model_path [str]: modelin kaydedildiği yol
		"""
		
		pred_label_list = []
		
		from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer, AutoModelForSequenceClassification
		
		tokenizer = AutoTokenizer.from_pretrained(model_path)   
		model = AutoModelForSequenceClassification.from_pretrained(model_path)
		self.nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
		
		for idx in tqdm(range(len(predict_text))):
			pred_label_list.append(int(self.nlp(predict_text[idx])[0]["label"].lstrip("LABEL_")))
		
		return pred_label_list


zs = Zeroshot()


app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def home():
	"""
	if request.method == 'POST':
		ad = request.form["name"]
		mail = request.form["email"]
		telefon = request.form["phone"]
		print("*"*50)
		print(ad,mail,telefon)
	"""
	return render_template("homepage.html")

@app.route("/demo", methods=['GET', 'POST'])
def demo():

	if request.method == 'POST':
		
		global result

		labels = request.form["candidate_labels"].split(',')
		text = request.form["text"]
		

		result = zs.predict(text,labels)[0]
		
		print(result)

	return render_template("submit.html")
     
if __name__ == "__main__":

	#app.debug = True
	app.run()
