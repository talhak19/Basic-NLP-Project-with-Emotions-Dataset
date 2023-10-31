import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def stopword_process(df):
    df = df.lower()

    #Kelimeleri tokenize etme
    words = word_tokenize(df)

    #Stopwords kaldırma 
    words = [word for word in words if word not in stop_words]

    return ' '.join(words)

