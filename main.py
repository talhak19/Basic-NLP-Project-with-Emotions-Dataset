import Data_Init.csv_class as csv_class
import Data_Stuff.data_info as data_info
import Data_Stuff.graphics as graphics
import Data_Cleaning.remove_duplicate as remove_duplicate
import Models.models as models
import Data_Cleaning.all_remove_process as allRemoveProcess


if __name__ == '__main__':
    

    train_data = csv_class.Data_Read("./data/train.txt")
    test_data = csv_class.Data_Read("./data/test.txt")
    val_data = csv_class.Data_Read("./data/val.txt")

    # data_info.data_info(train_data.df)
    # print("********************************************** END **********************************************************")
    # data_info.data_info(test_data.df)
    # print("********************************************** END **********************************************************")
    # data_info.data_info(val_data.df)

    #İşlenmemiş grafik versiyonları.
    graphics.emotion_count(train_data.df,"Train Graphic")
    graphics.emotion_count(val_data.df,"Validation Graphic")
    graphics.emotion_count(test_data.df,"Test Graphic")




    #Data info's
    # data_info.data_info(train_data)
    # data_info.data_info(val_data)
    # data_info.data_info(test_data)

####
    sample_text = ("I have been loving you since i saw you.")

    train_data.df["Text"] = allRemoveProcess.allRemoveProcess(train_data.df["Text"])
    train_data.df["Emotion"] = allRemoveProcess.allRemoveProcess(train_data.df["Emotion"])

    val_data.df["Text"] = allRemoveProcess.allRemoveProcess(val_data.df["Text"])
    val_data.df["Emotion"] = allRemoveProcess.allRemoveProcess(val_data.df["Emotion"])

    test_data.df["Text"] = allRemoveProcess.allRemoveProcess(test_data.df["Text"])
    test_data.df["Emotion"] = allRemoveProcess.allRemoveProcess(test_data.df["Emotion"])


    #Burada ise  verisetlerinde tekrar eden satırları - aynı duyguları ve tekrar eden satırlar - farklı duyguları çıkartacağız.
    train_data = remove_duplicate.duplicate_process(train_data.df)
    val_data = remove_duplicate.duplicate_process(val_data.df)
    test_data = remove_duplicate.duplicate_process(test_data.df)


    sample_text = allRemoveProcess.allRemoveProcessForText(sample_text)

    data_info.data_info(train_data)
    data_info.data_info(val_data)
    data_info.data_info(test_data)


    X_train = train_data['Text'].values
    y_train = train_data['Emotion'].values

    X_test = test_data['Text'].values
    y_test = test_data['Emotion'].values

    X_val = val_data['Text'].values
    y_val = val_data['Emotion'].values


    # ##MODELS
    # random_forest
    random_forest_model = models.Model(X_train,X_test,y_train,y_test,"random_forest",sample_text)
    random_forest_model.model_executer()

    #l_gbm
    l_gbm_model = models.Model(X_train,X_test,y_train,y_test,"l_gbm",sample_text)
    l_gbm_model.model_executer()

    #xgb
    xgb_model = models.Model(X_train,X_test,y_train,y_test,"xgb",sample_text)
    xgb_model.model_executer()
