import requests as req
from bs4 import BeautifulSoup
import re
import pandas as pd

def scraping():
    url = 'https://instabug.com/blog/mobile-game-publishers/'
    html = requests.get(url).content
    bs = BeautifulSoup(html, 'lxml')
    searching = bs.find_all('h3', class_= '')
    developer_list=[e.text.replace('\n','').replace('  ', '') for e in searching]
    top_developer = pd.DataFrame(developer_list,columns = ['top_developer'],)
    return top_developer

def extraerdatos():
    df = pd.read_csv('./appstore_games.csv', encoding='latin')
    df.columns = df.columns.to_series().apply(lambda x: x.strip())
    df.isnull().sum().sort_values().head()/17007
    df_reducido=df[["Name","User Rating Count","Price","Languages","Primary Genre",'Developer',]]
    return df_reducido

df_reducido= extraerdatos()
top_developer=scraping()
pd.concat([df_reducido, top_developer], axis=0)