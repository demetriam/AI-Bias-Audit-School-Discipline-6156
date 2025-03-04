# import requests
# import pandas as pd
# import time
# import nltk
# import re
# import ssl
# import re

# from nltk.sentiment import SentimentIntensityAnalyzer
# ssl._create_default_https_context = ssl._create_unverified_context
# requests.packages.urllib3.disable_warnings()

# nltk.download("vader_lexicon")
# sia = SentimentIntensityAnalyzer()
# API_KEY = "9a3eb90dcf01430997191d3e48fabba3"

# QUERIES = [
#     "school discipline punishment",
#     "student behavioral policies",
#     "zero tolerance policies in schools",
#     "restorative justice in education",
#     "impact of school suspensions",
#     "corporal punishment in schools",
#     "racial disparities in school discipline",
#     "positive behavioral interventions and supports",
#     "school-to-prison pipeline",
# ]

# FILTER_KEYWORDS = [
#     "school discipline", "suspension", "expulsion", "restorative justice",
#     "zero tolerance", "behavioral intervention", "school to prison pipeline",
#     "racial disparities in discipline", "student punishment", "school policy reform"
# ]

# EXCLUDED_SOURCES = [
#     "breitbart.com", "foxnews.com", "thegatewaypundit.com",
#     "infowars.com", "dailycaller.com"
# ]

# def is_relevant(article):
#     title = article.get("title", "") or ""  
#     description = article.get("description", "") or "" 
#     text = (title + " " + description).lower() 

#     return any(re.search(rf"\b{keyword}\b", text) for keyword in FILTER_KEYWORDS)

# def is_allowed_source(article):
#     url = article.get("url", "").lower()
#     return not any(source in url for source in EXCLUDED_SOURCES)

# def is_relevant_by_sentiment(article):
#     title = article.get("title", "") or ""
#     description = article.get("description", "") or ""
#     text = title + " " + description
#     sentiment = sia.polarity_scores(text)
#     return sentiment["compound"] < 0.5 

# NUM_PAGES = 5  
# all_articles = []

# for query in QUERIES:
#     print(f"\n Fetching articles for: {query}")
    
#     url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=relevancy&pageSize=100&apiKey={API_KEY}"
    
#     for page in range(1, NUM_PAGES + 1):
#         response = requests.get(url + f"&page={page}", verify=False)
#         data = response.json()

#         if "articles" in data:
#             articles = data["articles"]
#             filtered_articles = [
#                 article for article in articles
#                 if is_relevant(article) and is_allowed_source(article) and is_relevant_by_sentiment(article)
#             ]
#             all_articles.extend(filtered_articles)
#         time.sleep(2) 

# df = pd.DataFrame(all_articles).drop_duplicates(subset=["title"])
# df.to_csv("school_discipline_news_filtered.csv", index=False)



# I tried to use data scraping here 