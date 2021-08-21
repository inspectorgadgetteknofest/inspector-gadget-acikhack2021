from preprocess.text import Text

a = Text()

print(a.lower("MERHABA"))


from preprocess.twitter import Twitter

tw = Twitter()

tweet = "Onlar çok mutlu. @example"

print(tw.removeMention(tweet))



from preprocess.trainedModel import trainedModel

model = trainedModel()

text = "Çok mutsuzum."

label, score = model.sentAnalysis(text)

print("Label: ", label)
print("Score: ", score)


from preprocess.twitter import Twitter

tw = Twitter()

tw.getTweet(from_="jack")


