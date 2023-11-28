import requests

def news(category):
    token_key = "9842c8f4eeb446a995cb80f41222fee0"
    param = {
        'country' : "in",
        "apiKey" : token_key,
        "category" : category,
    }
    s=requests.get("http://newsapi.org/v2/top-headlines",param).json()
    articles = (s['articles'])
    title = []
    url = []
    # print(len(articles))
    for article in articles :
        title.append(article['title'])
        content = article['content']
        image = article['urlToImage']
        url.append(article['url'])
        description= article['description']
        # print("{0!r}".format(content))
        # print(repr(url))
    return title,url
        

def search(keyword):
    token_key = "9842c8f4eeb446a995cb80f41222fee0"
    param = {
        'q' : keyword,
        "apiKey" : token_key,
    }
    s=requests.get("http://newsapi.org/v2/everything",param).json()
    articles = (s['articles'])
    title = []
    url = []
    for article in articles :
        title.append(article['title'])
        content = article['content']
        image = article['urlToImage']
        url.append(article['url'])
        description= article['description']
    return title,url
