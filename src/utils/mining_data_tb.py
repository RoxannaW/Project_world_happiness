import pandas as pd
import numpy as np
import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import missingno
import time
import random
import json
import seaborn as sns
import matplotlib.pyplot  as plt

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
                        'Perceptions of corruption']]
                     
        return df

# adding column Year to each dataframe
def Add_year(df, year):

    df.insert(0, 'Year', year)

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



def clean_data_unemployment_rate(x):
    df_unemployment = x[['ref_area.label', 'time', 'obs_value']]
    df_unemployment.rename(columns={'ref_area.label':'Country', 'time':'Year', 'obs_value':'Unemployment_rate'}, inplace=True)
    df_unemployment.set_index("Country", inplace=True)
    df_unemployment = df_unemployment.pivot_table(values='Unemployment_rate', index=df_unemployment.index, columns='Year', aggfunc='first') 
    return df_unemployment


def join_df(df, df1, df2):
    complete_df = df.join(df1)
    complete_df = complete_df.join(df2)
    complete_df.rename(columns={ complete_df.columns[-1]: "Unemployment rate", complete_df.columns[-2]: "Peace index"}, inplace=True)

    print("Dataframes are joined")
    return complete_df


def to_datetime(df):
    df["Year"] = pd.to_datetime(df["Year"], format='%Y').dt.year
    print("Done")

def none_values(df):

    if len(df[df.isnull().any(axis=1)] != 0):
        print("\nPreview of data with null values:")
        display(df[df.isnull().any(axis=1)].head(3))
        missingno.matrix(df)
        plt.show()

def drop_column(df):
    df = df.drop("Unemployment rate", axis=1)
    return df

def show_duplicates(df):
    if len(df[df.duplicated()]) > 0:
        print("\n***Number of duplicated entries: ", len(df[df.duplicated()]))
        display(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)).head())
    else:
        print("\nNo duplicated entries found")