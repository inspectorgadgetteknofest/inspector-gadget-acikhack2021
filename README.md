# inspector-gadget-acikhack2021

## 1. ...
## 2. ...
## 3. ...
## 4. ...
## 5. Preprocess
<br>
Bu bölümde Türkçe Doğal Dil işleme projelerinde kullanılması muhtemel bütün ön işleme süreçlerini toplamaya çalıştık.

### Text
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
