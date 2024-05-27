import joblib
import globalVar
import pandas as pd

def predict3Helper(genre, region, console):
    # load model
    model = joblib.load('Model/prediction3/model_no_publishers.joblib')
    allRegions = ['JP ', 'NA ', 'Other ', 'PAL ']
    allConsoles = ['PS', 'X360', 'PS3', 'DS', 'Wii', 'PS2', 'GBA', 'PC', 'PS4', 'GBC', 'PSV', 'PSP',
            'XB', '3DS', 'SNES', 'GC', 'XOne', 'SAT', 'NS', 'GB', 'DC', 'WiiU', 'N64', 'PSN',
            'PCE', 'GEN', '3DO', 'NES', '2600', 'XBL', 'NG', 'WW', 'SCD', 'Mob', 'GG', 'VC', 'WS',
            'PCFX', 'OSX']
    if region != None:
        region_max = region
        y_max = -99999
        console_max = 'err'
        for consl in allConsoles:
            input_data = {
                'Genre': [genre],
                'Region': [region],
                'Console': [consl]
            }
            input_df = pd.DataFrame(input_data)
            y = model.predict(input_df)[0]
            if y > y_max:
                y_max = y
                console_max = consl
    else:
        console_max = console
        y_max = -99999
        region_max = 'err'
        for regs in allRegions:
            input_data = {
                'Genre': [genre],
                'Region': [regs],
                'Console': [console]
            }
            input_df = pd.DataFrame(input_data)
            y = model.predict(input_df)[0]
            if y > y_max:
                y_max = y
                region_max = regs
    
    return [region_max, console_max, y_max]

def testPredict3(genre, region, console):
    model = joblib.load('Model/prediction3/model_no_publishers.joblib')
    

    input_data = {
    'Genre': [genre],
    'Region': ['JP '],
    'Console': ['console']
    }

    input_df = pd.DataFrame(input_data)
    y = model.predict(input_df)[0]
    return y