[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17Y9V2PbN0M13nwvC_6XjRn2UlMvO_I8t?authuser=2#scrollTo=_DvMN8znn23s)

# Döküman Sınıflandırıcı

Bu projede amacımız; BERT, LSTM gibi derin öğrenme tabanlı sınıflandırıcı modellerine verilen girdilerin uzunluklarının (sequences) bir kısıtı olmasıdır. Bu kısıt BERT'te 512 token iken Large LSTM'de bu sayı 500'e çıkmaktadır.  Ancak verimiz bu sayılardan daha uzunsa ve herhangi bir kırpma-kısaltma işlemi gerçekleştirmek istemiyorsak bu durumda yardımınıza oluşturduğumuz proje yetişmekte.

## Installation

Oluşturduğumuz kütüphaneyi indirmek için :

```bash
pip install kütüphane
```

## Kullanım
Döküman (uzun metin) sınıflandırma projesini denemek için:

```python
import kütüphane

# returns 'words'
kütüphane.fonksiyon1('kelime')
```

## Veri
Veri seti olarak sayın Savaş Bey'in Türkçe diline kazandırmış olduğu [A Benchmark Data for Turkish Text Categorization (Turkish Text News Corpus)](https://www.kaggle.com/savasy/ttc4900) veri seti kullanılmıştır. Bu veri sınıf sayısı göz önüne alınarak 0.2 oranında eğitim ve test verisi olarak bölünmüştür.

## Elde Edilen Bulgular
Benchmark bir veri seti kullanarak eğitim boyunca ulaşılan en yüksek sonuçlar aşağıda yer almaktadır:

![](https://user-images.githubusercontent.com/56072259/130331430-e9d8c2c0-34b8-4084-91d9-aea1267a03a3.png)

Elde edilen en yüksek sonuçlar ise :



|   | precision | recall | f1-score | support |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| dunya  | 0.66  | 0.86 | 0.75  | 140  |
| ekonomi  | 0.78  | 0.71  | 0.74  | 140  |
| kultur  | 0.86  | 0.84  | 0.85  | 140  |
| saglik  | 0.88  | 0.90  | 0.89  | 140  |
| siyaset  | 0.79  | 0.74  | 0.77  | 140  |
| spor  | 0.92  | 0.87  | 0.90  | 140  |
| teknoloji  | 0.86  | 0.79  | 0.82  | 140  |
|  |   |  |  |  |
|accuracy|     |    |  0.82 |  980|
|macro avg|   0.82|   0.82|    0.82|   980|
|weighted avg| 0.82|  0.82 |   0.82 |  980|

## Örnek
```
Input : Nirvana ya solist oluyor the_beatles ile ünlenen paul mccartney bir geceliğine kurt cobain in yerine solit olarak gruba katılmıştır.
Output : kultur
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
