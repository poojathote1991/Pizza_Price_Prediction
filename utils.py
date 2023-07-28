import numpy as np
import pickle
import json
import config

class PizzaData():
    def __init__(self,diameter,topping,variant,size,extra_sauce,extra_cheese,extra_mushrooms,company):
        print("****************INIT FUNCTION********************")
        self.diameter=diameter
        self.topping=topping
        self.variant=variant
        self.size=size
        self.extra_sauce=extra_sauce
        self.extra_cheese=extra_cheese
        self.extra_mushrooms=extra_mushrooms
        self.company=company

    def __load_saved_data(self):
        model_file_name=config.MODEL_FILE_PATH
        with open(model_file_name,'rb') as f:
            self.model=pickle.load(f)
        json_file_name=config.JSON_FILE_PATH
        with open(json_file_name,'r') as f:
            self.proj_data=json.load(f)

    def get_predicted_price(self):
        self.__load_saved_data()
        diameter=self.proj_data['Diameter'][self.diameter]
        topping=self.proj_data['Topping'][self.topping]
        variant=self.proj_data['Variant'][self.variant]
        size=self.proj_data['Size'][self.size]
        extra_sauce=self.proj_data['Extra_sauce'][self.extra_sauce]
        extra_cheese=self.proj_data['Extra_cheese'][self.extra_cheese]
        extra_mushrooms=self.proj_data['Extra_mushrooms'][self.extra_mushrooms]
        company='company_'+ self.company
        company_index=self.proj_data['Column_name'].index(company)


        test_array=np.zeros([1,self.model.n_features_in_])
        test_array[0][company_index]=1
        test_array[0,0]=diameter
        test_array[0,1]=topping
        test_array[0,2]=variant
        test_array[0,3]=size
        test_array[0,4]=extra_sauce
        test_array[0,5]=extra_cheese
        test_array[0,6]=extra_mushrooms
        predicted_price=self.model.predict(test_array)[0]
        return predicted_price

