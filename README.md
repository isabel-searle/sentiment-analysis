# Sentiment Analysis in a US post presidential election period

This project is an ingenuous analysis of the sentiments from 286.099 tweets throgh all US without bias (no filters) during the post presidental election period.

![elections result](images/elections_map.png)

## The steps I followed were:

1. Twitter API
    - Get access.
    - Create a function to get more and more tweets.

2. Data cleaning and wrangling
    - Clean the data 
    - Add the coordenates and the points
    - Add the id state and id county to be readible by the plotly funtions.

3. Sentiment analysis

4. Create the maps according with the results of the analysis

<p align="center">
<img src="images/sentiment_map_.png" alt="sentiment_map" width="400"/>
</p>


5. Get the election result. I got the data from [Kaggle](https://www.kaggle.com/unanimad/us-election-2020)

6. Data cleaning and wrangling
    - Clean the data 
    - Add the coordenates and the points
    - Add the id state and id county to be readible by the plotly funtions.

7. Create the map according with the resuts

8. Create a correlation heatmap

<p align="center">
<img src="api/resources/corr_heatmap.png" alt="heatmap" width="600"/>
</p>


9. Create the wordclouds and compare given the results obtained in the lasts steps.
<p align="center">
<img src="images/cloud_usa.png" alt="sentiment cloud" width="500"/>
</p>
10. Build a web page with flask in order to present my project.

<p align="center">

<img src="images/web_1.png" alt="web" width="600"/>


<img src="images/web_2.png" alt="web" width="600"/>


<img src="images/web_3.png" alt="web" width="600"/>


</p>


## Tools and procedures:

- Data cleaning and wrangling
- API requests
- Data visualization
- Geolocation
- Webscraping
- Flask
- HTML
- CSS


- Libraries:

    - shapely
    - plotly
    - nltk
    - pandas
    - numpy
    - wordcloud
    - seaborn
    - scipy
    - tweepy



