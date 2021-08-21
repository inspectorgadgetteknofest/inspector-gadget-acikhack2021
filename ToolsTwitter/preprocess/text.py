import numpy as np
import re
import string




class Text():
    
    
    def __init__(self):
        self.lower_table = str.maketrans("ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZWXQ","abcçdefgğhiıjklmnoöprsştuüvyzwxq")
        self.noktalama_isaretleri = np.array(["...",".","?","!",":"])

        
    
    def lower(self, text):
        """
        Converts the input to lowercase. (Girdiyi küçük harflere dönüştürür.)

        Example: 
        
        Input:
        
        \ttext [string] => "MERHABA"
        
        Output:
        
        \ttext [string] => "merhaba"
        """
        return text.translate(self.lower_table)
    
    def removePunc(self, text): 
        """
        Removes punctuation in the input. (Girdi içerisindeki noktalama işaretlerini atar.)

        Example: 
        
        Input:
        
        \ttext [string] => "Daha mutlu olamam."
        
        Output:
        
        \ttext [string] => "Daha mutlu olamam"
        """
        
        return text.translate(str.maketrans('', '', string.punctuation))
    
    
    def sentTokenize(self, text):
        """
        Splits input into sentences. (Girdiyi cümlelere böler.)

        Example: 
        
        Input:
        
        \ttext [string] => "Daha mutlu olamam. Bu akşam."
        
        Output:
        
        \tsentences [list <string>] => ["Daha mutlu olamam.", "Bu akşam."]
        """
       
        return re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s",text)
        
    def wordTokenize(self, text):
        """
        Splits input into words. (Girdiyi kelimelere böler.)

        Example: 
        
        Input:
        
        \ttext [string] => "Daha mutlu olamam. Bu akşam."
        
        Output:
        
        \twords [list <string>] => ["Daha", "mutlu", "olamam", "Bu", "akşam"]
        """
        
        return self.removePunc(text).split()
    
    def dropEmail(self, text):
        """
        Remove email in input text. (Girdideki emailleri atar.)

        Example: 
        
        Input:
        
        \ttext [string] => "example@example.com adresinden ulaşabilirsiniz."
        
        Output:
        
        \ttext [string] => "adresinden ulaşabilirsiniz."
        """
        
        return re.sub(r"(\S*@\S*\s?)","",text)
    
    
    
    def dropURL(self, text):
        """
        Remove URL in input text. (Girdideki URLleri atar.)

        Example: 
        
        Input:
        
        \ttext [string] => "www.example.com adresinden ulaşabilirsiniz."
        
        Output:
        
        \ttext [string] => "adresinden ulaşabilirsiniz."
        """
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'www.\S+', '', text)
        return re.sub(r"[^\s]*(?:\.(com|org)(\S*))","",text)
    
    
    
    def justValid(self, text):
        """
        It just keeps the valid characters. You can use droping emoji. (Sadece doğru karakterleri tutar. Emojileri kaldırırken kullanabilirsiniz.)

        Example: 
        
        Input:
        
        \ttext [string] => "Hi! 😊"
        
        Output:
        
        \ttext [string] => "Hi! "
        """

        return re.sub(r'[^\x00-\x7fğüışöçĞÜIİŞÖÇ0-9]','',text)