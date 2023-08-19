import pickle
import numpy as np

brand = {
        0:"Audi",
        1:"Hyundai Creta",
        2:"Mahindra Scorpio",
        3:"Rolls Royce",
        4:"Swift",
        5:"Tata Safari",
        6:"Toyota Innova"
        }

def carbrandPredictor(model, hog):
    predictResult = model.predict(np.array(hog).reshape(1,-1))
    return {'Brand:':brand[predictResult[0]]}
# hog