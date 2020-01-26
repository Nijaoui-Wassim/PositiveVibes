#créé par wiiiw TEAM
#Nijaoui Wassim -Nijaoui Khalil - Alladin Aroua

#Module Used SentimentIntensityAnalyzer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()



def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    negative_value = float(snt['neg'])
    positive_value = float(snt['neu'])
    neutral_value = float(snt['pos'])
    compound_value = float(snt['compound'])
    #print('negative_value',negative_value)
    #print("{:-<40} {}".format(sentence, str(snt)))
    if compound_value >0:
        return 'Positive statement ', compound_value
    elif compound_value <0:
        return 'Negative statement ', compound_value
    else:
        return 'Neutral statement ', compound_value
