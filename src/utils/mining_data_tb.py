# Renaming columns so all dataframes have the same columns names. 
def Change_columns(df):
    try:
        df.rename(columns={'Happiness Rank': 'Overall rank', 'Happiness Score': 'Score',
        'Economy (GDP per Capita)':'GDP per capita', 'Family':'Social support',
        'Health (Life Expectancy)': 'Healthy life expectancy', 'Freedom': 'Freedom to make life choices', 
        'Trust (Government Corruption)': 'Perceptions of corruption'}, inplace=True)
    except: 
        pass
    try:
        df.rename(columns={'Happiness.Rank': 'Overall rank', 'Happiness.Score': 'Score', 
        'Economy..GDP.per.Capita.':'GDP per capita', 'Family':'Social support', 
        'Health..Life.Expectancy.': 'Healthy life expectancy', 'Freedom': 'Freedom to make life choices', 
        'Trust..Government.Corruption.': 'Perceptions of corruption'}, inplace=True)
    except:
        pass
    try:
        df.rename(columns={'Country or region': 'Country'}, inplace=True)
    except:
        pass


## clean dataframes to set country as index and keep only selected columns
def Filter_dataframe(df):
        df.set_index("Country", inplace=True)
        df = df[['Overall rank', 'Score', 'GDP per capita', 'Social support',
                        'Healthy life expectancy', 'Freedom to make life choices', 'Generosity',
                        'Perceptions of corruption', 'Year']]
                     
        return df

# adding column Year to each dataframe
def Add_year(df, year):

    df["Year"] = year

    print("done")
    return df

def Test():
    print("Hola")

def Clean_data_peace_index(df):
    df = df[['Country', '2019 rank', '2019 score[12]', '2018 rank', '2018 score[13]', '2017 rank', '2017 score[2]',
             '2016 rank', '2016 score[14]','2015 rank', '2015 score[15]']]
    df.set_index("Country", inplace=True)
    df.rename(columns={'2019 score[12]':'2019 score', '2018 score[13]':'2018 score', '2017 score[2]':'2017 score', 
             '2016 score[14]':'2016 score', '2015 score[15]':'2015 score'}, inplace=True) 

    print("done")
    return df

def Clean_data_unemployment(df):
    df = df[['ref_area.label', 'time', 'obs_value']]
    df.rename(columns={'ref_area.label':'Country', 'time':'Year', 'obs_value':'Unemployment_rate'}, inplace=True)
    df.set_index("Country", inplace=True)
    
    print("done")
    