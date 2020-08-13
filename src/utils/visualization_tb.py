import os, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot  as plt
from IPython.display import Image
import plotly.express as px

os.path.abspath('')
root_path = os.path.dirname(os.path.abspath(''))
sys.path.append(root_path)

def treemap_show(df):
    print("Done")
    fig = px.treemap(df, path=[df.index], 
                values='Score',title="Country names based on Happiness score")
    fig.show()
    

def test():
    print("I'm working")

def top10_show(df):
    fig = px.bar(data_frame = df.nlargest(10,"Score"),
             y=df.nlargest(10,"Score").index,
             x="Score",
             orientation='h',
             color=df.nlargest(10,"Score").index,
             text="Score",
             color_discrete_sequence=px.colors.qualitative.D3)
    fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})

    fig.update_traces(texttemplate='%{text:.2s}', 
                  textposition='inside', 
                  marker_line_color='rgb(255,255,255)', 
                  marker_line_width=2.5, 
                  opacity=0.7)
    fig.update_layout(width=800,
                  showlegend=False,
                  title="Top 10 happiest countries",)
    fig.show()

def lowest10_show(df):
    fig1 = px.bar(data_frame = df.nsmallest(10,"Score"),
             y=df.nsmallest(10,"Score").index,
             x="Score",
             orientation='h',
             color=df.nsmallest(10,"Score").index,
             text="Score",
             color_discrete_sequence=px.colors.qualitative.D3)
    fig1.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})

    fig1.update_traces(texttemplate='%{text:0.2f}',
                  textposition='inside', 
                  marker_line_color='rgb(255,255,255)', 
                  marker_line_width=2.5, 
                  opacity=0.7)
    fig1.update_layout(width=800,
                  showlegend=False,
                  title="Top 10 unhappiest countries",)
    fig1.show()

def score_order_bar(df):
    fig = px.bar(df, x=df.index, y='Score',color='Score',height=800)
    fig.update_layout(title='Countries in order of Happiness Score',titlefont_size=20)
    fig.show()

#Scatterplot to show a column vs the country happiness score and
    #size of the bubble dependent on a value of column of choice
def scatter_show(df, column):
    fig = px.scatter(df, x=column, y="Score",
	         size="Social support", color=df.index,height=800,
                 hover_name=df.index, log_x=True, size_max=60)
    fig.update_layout(title="Happiness Score vs {}".format(column))
    fig.show()

def distribution_show(df):
    fig = px.histogram(df["Score"],
                   marginal="box")
    fig.update_traces(opacity=0.7,
                      marker_line_color='rgb(255,255,255)', 
                      marker_line_width=2.5
                      )
    fig.update_layout(showlegend=False,
                  title="Distribution of happiness scores",
                  width=800)
    fig.show()

def trend_rank(df, column):
    fig=px.line(df,x='Year',y=column, color=df.index,template="plotly_dark")
    fig.update_layout(title="Trend of {}".format(column))
    fig.show()