##
print("hello world")

##
import pandas
from pathlib import Path

csv_file_path = Path('./csv-files/data.csv')
news_data = pandas.read_csv(csv_file_path)

news_data.head()

## print the column names
news_data.columns

## get source name with the highest number of articles

print('Source name with the highest number of articles:')
news_data['source_name'].value_counts().idxmax()


## laod news rating 

news_rating = pandas.read_csv(Path('./csv-files/rating.csv'))

news_rating.head()

## print the column names

news_rating.columns

## load news traffic

news_traffic = pandas.read_csv(Path('./csv-files/traffic.csv'))

news_traffic.head()

## print the column names

news_traffic.columns
## print the column of the best GlobalRank

print('Website with the highest traffic:')

top_websites = news_traffic.sort_values(by='GlobalRank', ascending=True)

news_traffic.loc[news_traffic['GlobalRank'].idxmin(), 'Domain']

## 



## load news domain location

news_domain_location = pandas.read_csv(Path('./csv-files/domains_location.csv'))

news_domain_location.head()

## print the column names

news_domain_location.columns

##

countries_media_counts = news_domain_location.groupby('Country').size().sort_values(by='Country')



