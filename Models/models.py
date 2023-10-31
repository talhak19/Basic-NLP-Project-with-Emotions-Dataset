from sklearn import metrics
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report


class Model:

        def __init__(self,X_train,X_test,y_train,y_test,model,sample_text):
                self.X_train = X_train
                self.x_test = X_test
                self.y_train = y_train
                self.y_test = y_test
                self.model = model
                self.sample_text = sample_text


        def model_executer(self):
                if self.model == "random_forest":
                        self.R_Forest()
                        
                elif self.model == "l_gbm":
                        self.Light_GBM()
                        
                elif self.model == "xgb":
                    self.XGBoost()

                else:
                        print("Gecerli bir model ismi giriniz....(random_forest , l_gbm, XGB)")
        

        def train_model(self,model):
                if self.model == 'xgb':
                        #xgbClassifier bizden str beklemiyor. [0,1,2,3,4,5] olması icin bunu yapıyoruz.
                        le = LabelEncoder()
                        self.y_train = le.fit_transform(self.y_train)
                        self.y_test = le.fit_transform(self.y_test)
                
                print("************************",self.model.upper(),"************************")
                # TF-IDF vectorunu bir pipeline ile verilen modele geçiriyoruz.
                text_clf = Pipeline([('vect',TfidfVectorizer()),
                                    ('clf', model)])
                # Train islemi
                text_clf.fit(self.X_train, self.y_train)
                return text_clf
        
        def R_Forest(self):

                random_forest = RandomForestClassifier(random_state=0)
                model_output = self.train_model(random_forest)

                #test dataları ile tahmin al
                y_pred=model_output.predict(self.x_test)

                random_forest_accuracy = accuracy_score(self.y_test, y_pred)
                print('Accuracy: ', random_forest_accuracy,'\n')

                #classify report
                print(classification_report(self.y_test, y_pred))


                #Sample data çıktısı 
                y_pred_sample=model_output.predict([self.sample_text])
                print(self.sample_text," textinin",self.model," tahmini: ",y_pred_sample)


        def Light_GBM(self):
                l_gbm = lgb.LGBMClassifier(random_state=0)
                model_output = self.train_model(l_gbm)

                #test dataları ile tahmin al
                y_pred=model_output.predict(self.x_test)

                l_gbm_accuracy = accuracy_score(self.y_test, y_pred)
                print('Accuracy: ', l_gbm_accuracy,'\n')

                #classify report
                print(classification_report(self.y_test, y_pred))

                #Sample data çıktısı 
                y_pred_sample=model_output.predict([self.sample_text])
                print(self.sample_text," textinin",self.model," tahmini: ",y_pred_sample)




        def XGBoost(self):

                xgb = XGBClassifier(booster='gbtree')
                model_output = self.train_model(xgb)

                #test dataları ile tahmin al
                y_pred=model_output.predict(self.x_test)

                xgb_accuracy = accuracy_score(self.y_test, y_pred)
                print('Accuracy: ', xgb_accuracy,'\n')

                #classify report
                print(classification_report(self.y_test, y_pred))


                #Sample data çıktısı 
                y_pred_sample=model_output.predict([self.sample_text])

                #XGB Classifier'ı çalıştırırken str vermediğimiz için burada tekrar Label karşılığını alma işlemi yapıyoruz.
                label_dict = {0: "Anger", 1: "Fear", 2: "Joy", 3: "Love", 4: "Sadness",5:"Surprise"}
                y_pred_sample = [label_dict[y] for y in y_pred_sample]

                print("'",self.sample_text,"'"," textinin",self.model," tahmini: ",y_pred_sample)
