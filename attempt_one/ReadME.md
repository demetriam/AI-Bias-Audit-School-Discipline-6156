Overview of My Experiment Attempts

This folder contains all the different approaches I attempted to run my experiment.

data_scraping.py

I attempted to use web scraping and sentiment analysis to collect text data from 
online news sources, process it, and analyze the sentiment of the retrieved content. 
However, this approach did not work as expected. The articles returned were often 
irrelevant to my specified queries and keywords. Many were unrelated to the 
intended topics and instead covered subjects such as anti-abortion movements 
and political affiliations.

crdc_anaylsis.py

Here, I tried analyzing data related to school suspensions using the CRDC dataset. 
My goal was to preprocess the data, split it into training and test sets, and evaluate
a machine learning models performance using a classification report. However, the 
dataset was too large, and my computer did not have enough memory to run the 
model on the CSV file.

merge_sqlite.py
To overcome memory issues, I attempted to process and store the CRDC data in an 
SQLite database. Unfortunately, my computer still ran out of memory when executing 
this approach, forcing me to abandon the idea.

synthetic_data.py

Since working with real-world data proved too resource-intensive, I pivoted to 
generating and analyzing synthetic school discipline data. 
This script creates a dataset, trains a machine learning model to predict outcomes 
based on key features, and evaluates the models performance using a classification 
report. This approach allowed me to explore bias in school discipline predictions 
without the memory limitations posed by the CRDC dataset.

