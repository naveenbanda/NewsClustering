
# coding: utf-8

# In[28]:

# import packages
import requests
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from matplotlib import pyplot as plt


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[29]:

# a function to extract the sources I'll be analyzing. I'll focus on the english ones
def getSources():
    source_url = 'https://newsapi.org/v1/sources?language=en'
    response = requests.get(source_url).json()
    sources = []
    for source in response['sources']:
        sources.append(source['id'])
    return sources


# In[ ]:




# In[ ]:




# In[ ]:




# In[30]:

# let's see what news sources we have
sources = getSources()
print('number of sources :', len(sources))
print('sources :', sources)


# In[ ]:




# In[ ]:




# In[31]:

def mapping():
    d={}
    response=requests.get("https://newsapi.org/v1/sources?language=en")
    response=response.json()
    for s in response['sources']:
        d[s['id']]=s['category']
    return d


# In[ ]:




# In[ ]:




# In[32]:

m=mapping()
print('category of reuters:', m['reuters'])
print('category of techcrunch:', m['techcrunch'])



# In[ ]:




# In[ ]:




# In[33]:

print('categories:', list(set(m.values())))


# In[ ]:




# In[34]:

def category(source,m):
    try:
        return m[source]
    except:
        return 'NC'


# In[ ]:




# In[35]:

def cleanData(path):
    data=pd.read_csv(path)
    data=data.drop_duplicates('url')
    data.to_csv(path,index=False)


# In[ ]:




# In[37]:

def getDailyNews():
    sources = getSources()
    key = 'de90302e18eb48c19dec162d8fe900a3'
    url = 'https://newsapi.org/v1/articles?source={0}&sortBy={1}&apiKey={2}'
    responses = []
    for i, source in tqdm(enumerate(sources)):
        try:
            u = url.format(source, 'top',key)
            response = requests.get(u)
            r = response.json()
            for article in r['articles']:
                article['source'] = source
            responses.append(r)
        except:
            u = url.format(source, 'latest', key)
            response = requests.get(u)
            r = response.json()
            for article in r['articles']:
                article['source'] = source
            responses.append(r)
      
    news = pd.DataFrame(reduce(lambda x,y: x+y ,map(lambda r: r['articles'], responses)))
    news = news.dropna()
    news = news.drop_duplicates()
    d = mapping()
    news['category'] = news['source'].map(lambda s: category(s, d))
    news['scraping_date'] = datetime.now()

    try:
        aux = pd.read_csv('news.csv')
    except:
        aux = pd.DataFrame(columns=list(news.columns))
        aux.to_csv('news.csv', encoding='utf-8', index=False)

    with open('news.csv', 'w') as f:
        news.to_csv(f, header=True, encoding='utf-8', index=False)

    cleanData('news.csv')
    print('Done')
    
print("OK")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[38]:

if __name__ == '__main__':
    getDailyNews()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



