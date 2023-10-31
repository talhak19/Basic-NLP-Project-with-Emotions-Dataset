import re

def rm_punctuations(df):

   ## Metinde bunlarla alakalı herhangi bir sey var ise, bosluk yap.
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,،-./:;<=>؟?@[\]^_`{|}~"""), ' ', df)
    text = text.replace('؛',"", )
    
    #\s fazla boslugu ifade eder, bunu tek boslukla sub ediyoruz.
    text = re.sub('\s+', ' ', text)
    text =  " ".join(text.split())
    return text.strip()