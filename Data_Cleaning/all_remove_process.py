import Data_Cleaning.remove_duplicate as remove_duplicate
import Data_Cleaning.remove_stopwords as remove_stopwords
import Data_Cleaning.remove_punctuations as remove_punctuations
import Data_Cleaning.remove_numbers as remove_numbers


def allRemoveProcess(df):
    #İngilizcede yer alan stopwords kelimeleri kaldıralım, (nltk)
    df = df.apply(remove_stopwords.stopword_process)

    #Text digit ise almıyoruz.
    df = df.apply(remove_numbers.rm_numbers)

    #Noktalama isaretlerini kaldıralım.
    df = df.apply(remove_punctuations.rm_punctuations)
    
    return df

def allRemoveProcessForText(text):
    text =remove_stopwords.stopword_process(text)
    text =remove_numbers.rm_numbers(text)
    text =remove_punctuations.rm_punctuations(text)

    return text