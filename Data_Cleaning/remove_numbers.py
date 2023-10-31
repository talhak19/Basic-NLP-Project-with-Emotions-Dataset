
def rm_numbers(df):
    #Eğer o text digit ise almıyoruz.
    text=''.join([i for i in df if not i.isdigit()])
    
    return text