import re
import os   


class Twitter():
    def __init__(self):
        pass
    
    def removeHastag(self, tweet):
        """
        Remove hastag in a tweet. (Tweet içerisindeki hastag'i kaldırır.)

        Example: 
        
        Input:
        
        \ttext [string] => "Merhaba #Hello"
        
        Output:
        
        \ttext [string] => "Merhaba"
        """
        return re.sub(r"#\S+","", tweet)
    
    
    def removeMention(self, tweet):
        """
        Remove mention in a tweet. (Tweet içerisindeki mention'ı kaldırır.)

        Example: 
        
        Input:
        
        \ttext [string] => "Merhaba @example"
        
        Output:
        
        \ttext [string] => "Merhaba"
        """

        return re.sub(r"@\S+","", tweet).strip()
    
    def removeRT(self, tweet):
        """
        Remove retweet in a tweet. (Tweet içerisindeki retweet'i kaldırır.)

        Example: 
        
        Input:
        
        \ttext [string] => "rt Bugün hava çok güzel"
        
        Output:
        
        \ttext [string] => "Bugün hava çok güzel"
        """

        return re.sub(r"\brt\b","", tweet)
    
    def getTweet(self, q = "",  from_ = "", maxResult = 500, since = "", until = "", showQuery = True):
        """
        Get retweet using snscrape library. (snscrape kütüphanesini kullanarak tweet toplar.)
        
        Params:
        
        * q: Query word. (Sorgu kelimesi)
        
        * from_: Twitter user name. Ex. jack (Twitter kullanıcı adı. Örn. jack)
        
        * maxResult: Count of tweets. (Tweet sayısı)
        
        * since: Start date. Usage yyyy-mm-dd. (Başlangıç tarihi. Kullanımı yyyy-mm-dd.) 

        * until: Finish date. Usage yyyy-mm-dd. (Bitiş tarihi. Kullanımı yyyy-mm-dd.)
        
        * showQuery: snscrape query (snscrape sorgusu)
        
        
        Example: 
        
        Input:
        
        \ttext (query) 
        
        Output:
        
        \tfile (json) 
        """
        
        if until != "": until = " until:" + until
        
        if from_ != "": from_ = " from:" + from_
        
        if since != "": since = "--since " + since
        
        if showQuery:
        
            # Using OS library to call CLI commands in Python
            print(f'snscrape --jsonl --max-results {maxResult} {since} twitter-search "{q}{until}{from_}" > text-query-tweets.json')
            
            
        os.system(f'snscrape --jsonl --max-results {maxResult} {since} twitter-search "{q}{until}{from_}" > text-query-tweets.json')
