import json
import requests
    
class trainedModel():   
    
    def __init__(self):
        self.SENT_ANALYSIS_API_URL = "https://api-inference.huggingface.co/models/adresgezgini/Finetuned-SentiBERtr-Pos-Neg-Reviews"
        self.sent_analysis_headers = {"Authorization": "Bearer api_gxjjPVmHDGvBlYfwPqRkzgecnMbPXjWAaY"}
        self.GENERATE_API_URL = "https://api-inference.huggingface.co/models/adresgezgini/turkish-gpt-2"
        self.generate_headers = {"Authorization": "Bearer api_gxjjPVmHDGvBlYfwPqRkzgecnMbPXjWAaY"}
    
    def sentAnalysis(self,text):
        """
        Calculates the emotion of the input using the trained model. It outputs label and score value. (Eğitilmiş model kullanılarak girdinin duygusunu hesaplar. Çıktı olarak duygu ve skor değerini verir.)

        Trained model: https://huggingface.co/savasy/bert-base-turkish-sentiment-cased
        
        Example: 
        
        Input:
        
        \ttext [string] => "Daha mutlu olamam. Bu akşam."
        
        Output:
        
        \tlabel [string] => "negative" \n
        \tscore [int] => 0.8
        """
        
        data = json.dumps({"inputs":text})
        response = requests.request("POST", self.SENT_ANALYSIS_API_URL, headers=self.sent_analysis_headers, data=data)
        
        result = json.loads(response.content.decode("utf-8"))[0][0]
        
        return result["label"], result["score"]
        

    def generate(self,text):
        """
        Generates text based on input with a trained GPT-2 model. Returns the produced text as output. (Eğitilmiş GPT-2 modeliyle girdiye dayalı metin üretir. Çıktı olarak üretilmiş metni verir.)

        Trained model: https://huggingface.co/adresgezgini/turkish-gpt-2
        
        Example: 
        
        Input:
        
        \ttext [string] => "Sakince arkana dön bir bak"
        
        Output:
        
        \tlabel [string] => "Sakince arkana dön bir bak ..." 
        """
        
        data = json.dumps({"inputs":text})
        response = requests.request("POST", self.GENERATE_API_URL, headers=self.generate_headers, data=data)
        result = json.loads(response.content.decode("utf-8"))[0]
        
        return result["generated_text"]