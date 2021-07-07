import re   


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