
def duplicate_process(df):
    #Burada sadece hem text hem emotion eşitse siliyoruz.
    indexs = df[df.duplicated() == True].index
    df.drop(indexs,axis=0,inplace=True)
    df.reset_index(inplace=True,drop=True)

    #Burada ise text eşitliğine de bakıyoruz ki aynı texte farklı duygu yazılmasın.
    indexs2 = df[df["Text"].duplicated()==True].index
    df.drop(indexs2,axis=0,inplace=True)
    df.reset_index(inplace=True,drop=True)

    return df