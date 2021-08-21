# ZEROSHOT + BERT

Bu bölümde Zeroshot+BERT yapısını kullanarak oluşturduğumuz pipeline ile elinizdeki metinleri otomatik bir şekilde etiketlemeyi amaçladık. Verisetiniz belirlediğiniz sınıflarla eğitilmiş zeroshot ile tahminlenir. Belirlenen eşik değerin üzerindeki değerlerle oluşuturulan rafine veriseti ile BERT modeli eğitilir. Bu sayede etiketlenmemiş veri seti üzerinde en doğru tahmini yapabilen bir yapı oluşturulmuş olur.

<p align="center">
  <img src="https://github.com/inspectorgadgetteknofest/inspector-gadget-acikhack2021/blob/main/Zeroshot/images/diagram.png">
</p>


### 1.1 Zeroshot:
Zeroshot modeli önce büyük bir külliyat ile  gözetimsiz öğrenme yöntemiyle eğitilir, cosine similarity ile dil yapısını ve kelimeler arasındaki anlamsal bağı öğrenmiş olur. Eğitilmiş model sonucunda verilen metni istenilen sınıflar arasında en uygun olanı ile eşleştirir.

#### Kaynak: https://joeddav.github.io/blog/2020/05/29/ZSL.html

### 1.2 BERT:
Devlin vd. tarafından geliştirilen transformatörlerden çift yönlü kodlayıcı gösterimlere sahip olan BERT modeli ile birlikte, etiketlenmemiş metinlerin derin çift yönlü temsillerinin önceden eğitimi sırasında tüm katmanlarda sağ ve sol bağlam bilgilerinin dahil edilmesi sağlanmaktadır. Model, sonrasında ince ayar yapılarak göreve özgü şekilde eğitilebilmektedir. Bu görevler soru cevaplama, duygu analizi, metin sınıflandırma ve adlandırılmış varlık tanıma gibi farklı çeşitlerde olabilir.

#### Kaynak: https://arxiv.org/abs/2106.01735

### 1.3 Eğitim ve test aşamasında kullanılan veri setleri ve sonuç değerleri:

  #### a. Turkish sentiment analysis:
  Veriseti içerisinde Pozitif, Negatif ve Nötr olmak üzere 3 sınıf barındırır. Bu görevde Pozitif ve Negatif etikeltli veriler ile işlem yapılmıştır. >=0.85 olacak şekilde eşik değer belirlenmiş ve elde edilen veriler ile BERT modeli eğitilmiştir. Eğitilen BERT modelinin test verisetindeki doğruluk değeri % 99 olarak hesaplanmıştır.
  
  #### b. ttc-4900 Multiclass Text Classification: <a href= "https://www.kaggle.com/savasy/ttc4900">Link</a>
  Kemik grup tarafından oluşturulan veri seti içerisinde "Siyaset", "Dünya" gibi 7 benzersiz sınıf ve 4539 satır veri barındırır. Bu veriseti kullanılarak yapılan Zeroshot prediction kısmında >=0.85 olacak şekilde eşik değer belirlenmiş ve elde edilne veriler ile BERT modeli eğitilmiştir. BERT modelinin test verisetindeki doğruluk değeri %94 olarak hesaplanmıştır.
  
  
