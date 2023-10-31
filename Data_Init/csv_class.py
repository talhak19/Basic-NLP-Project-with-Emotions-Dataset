import pandas as pd
import warnings


class Data_Read():

    def __init__(self,data):
        # pd.set_option('max_column', None)
        self.df = pd.read_csv(data, names=['Text', 'Emotion'], sep=';')
