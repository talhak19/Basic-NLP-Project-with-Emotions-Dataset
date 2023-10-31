import seaborn as sns
import matplotlib.pyplot as plt

def emotion_count(df,name):
    plt.figure(figsize=(8,4))
    sns.countplot(x='Emotion', data=df)
    plt.title(name)

    plt.show()