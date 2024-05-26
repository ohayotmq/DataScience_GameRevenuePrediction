import joblib
import globalVar
import csv

def predict3Helper(genre, region, console):
    # load model
    model = joblib.load('Model/prediction3/...')

    genre = globalVar.genreEncoder.transform([genre])[0]
    allRegions = globalVar.regionEncoder.classes_
    allConsoles = globalVar.consoleEncoder.classes_
    if region != None:
        region_max =region
        y_max = -99999
        console_max = 'no'
        for consl in allConsoles:
            x = [[genre, globalVar.regionEncoder.transform([region])[0], globalVar.regionEncoder.transform([consl])[0]]]
            y = model.predict(x)[0]
            if y > y_max:
                y_max = y
                console_max = consl
    else:
        console_max = console
        y_max = -99999
        region_max = 'no'
        for regs in allRegions:
            x = [[genre, globalVar.regionEncoder.transform([console])[0], globalVar.regionEncoder.transform([regs])[0]]]
            y = model.predict(x)[0]
            if y > y_max:
                y_max = y
                region_max = regs
    
    return [region_max, console_max, y_max]