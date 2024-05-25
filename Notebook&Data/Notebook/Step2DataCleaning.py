
def dataCleaning():

    import pandas as pd

    raw_data = pd.read_csv('../Data/game_info.csv')
    raw_data

    pd.options.display.max_rows = 1000
    pd.options.display.max_columns = None

    df = raw_data.copy()
    df

    df.info()


    pd.unique(df['Units Sold'])

    #Task 1
    df = df.drop(['Developer(s)'], axis = 1)
    df

    df = df.drop(['Units Sold'], axis = 1)
    df


    df['Total Sales'] = df['Total Sales'].fillna(0)
    df

    df = df[df['Total Sales'] != 0]
    df

    df = df[df['Total Sales'] != '0.00m']
    df

    df['NA Sales'] = df['NA Sales'].fillna('0.00m')
    df['PAL Sales'] = df['PAL Sales'].fillna('0.00m')
    df['JP Sales'] = df['JP Sales'].fillna('0.00m')
    df['Other Sales'] = df['Other Sales'].fillna('0.00m')
    df

    df.info()

    df['Release Date'] = df['Release Date'].fillna(0)
    df = df[df['Release Date'] != 0]
    df

    df.info()

    df_task4 = df.copy()
    df_task4.index = range(len(df_task4.index))
    df_task4

    df_task4['Total Sales'] = df_task4['Total Sales'].str.replace('m','').astype(float)
    df_task4['NA Sales'] = df_task4['NA Sales'].str.replace('m','').astype(float)
    df_task4['PAL Sales'] = df_task4['PAL Sales'].str.replace('m','').astype(float)
    df_task4['JP Sales'] = df_task4['JP Sales'].str.replace('m','').astype(float)
    df_task4['Other Sales'] = df_task4['Other Sales'].str.replace('m','').astype(float)
    df_task4

    #Before converting to datetime, we stripped 'rd', 'st', 'nd', etc from the day of the week
    df_task4['Release Date'] = df_task4['Release Date'].str[:2] + df_task4['Release Date'].str[4:]
    df_task4['Release Date'] = pd.to_datetime(df_task4['Release Date'], format = '%d %b %y')
    df_task4

    df_task5 = df_task4.copy()
    df_task5

    #First months
    list_months = []
    for i in range(len(df_task5)):
        list_months.append(df_task5['Release Date'][i].month)
    list_months

    len(list_months)

    #Next years
    list_years = []
    for i in range(len(df_task5)):
        list_years.append(df_task5['Release Date'][i].year)
    list_years


    len(list_years)


    df_task5['Release Month'] = list_months
    df_task5['Release Year'] = list_years
    df_task5

    df_task5 = df_task5.drop(['Release Date'], axis = 1)
    df_task5


    df_task5.columns = ['Title', 'Genre', 'Console', 'Publisher', 'Total Sales (m)', 'NA Sales (m)', 'EU Sales (m)', 'JP Sales (m)',
                        'Other Sales (m)', 'Release Month', 'Release Year']
    df_task5


    df_task5['Genre'] = df_task5['Genre'].str.replace('+',' ')
    df_task5

    df_cleaned = df_task5.copy()
    df_cleaned.head(10)


    df_cleaned.info()


    df_cleaned.to_csv('../Data/game_info_cleaned.csv', index = False, header = True, mode='w')
    df_cleaned.to_excel('../Data/game_info_cleaned.xlsx', index = False, header = True, engine='xlsxwriter')


#Chạy file này bằng cách gọi hàm: dataCleaning()

dataCleaning()