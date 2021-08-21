# Turkkish NLP Toolkit

<p align="center">
  <img src="https://github.com/inspectorgadgetteknofest/inspector-gadget-acikhack2021/blob/main/ToolsTwitter/images/Inspector-Gadget.png">
</p>



Bu bölümde Türkçe Doğal Dil işleme projelerinde kullanılması muhtemel bütün ön işleme süreçlerini toplamaya çalıştık.

### 1. Text
* lower: Metni küçük harflere çevirir.
* removePunc: Metin içerisindeki noktalama işaretlerini atar.
* sentTokenize: Metni cümlelere böler.
* wordTokenize: Metni kelimelere böler.
* dropEmail: Metin içerisindeki e-mail'leri atar.
* dropURL: Metin içerisindeki URL'leri atar.
* justValid: Metin içerisinde sadece yazı karakteri ve sayı karakteri kalacak şekilde düzenler.

#### Nasıl kullanılır?
```python
from preprocess.text import Text

a = Text()

print(a.lower("MERHABA"))
```
#### Output:
```python
"merhaba"
```
<br>

### 2. Twitter
* removeHastag: Tweet içerisindeki hastagleri (#) atar.
* removeMention: Tweet içerisindeki mentionları (@...) atar.
* removeRT: Tweet içerisindeki RT'leri atar.
* getTweet: Verilen parametrelere göre tweet toplar.


#### Nasıl kullanılır?
```python
from preprocess.twitter import Twitter

tw = Twitter()

tweet = "Onlar çok mutlu. @example"

print(tw.removeMention(tweet))
```
#### Output:
```python
"Onlar çok mutlu."
```
<br>

#### Nasıl kullanılır? (getTweet)
```python
from preprocess.twitter import Twitter

tw = Twitter()

tw.getTweet(from_="jack")
```
Çıktı olarak  dosyası oluşturur. Bu dosyayı okumak için:

```python
import pandas as pd

df = pd.read_json('text-query-tweets.json', lines=True)
```


### References:
* https://github.com/JustAnotherArchivist/snscrape
