# Group 2 Midterm Project Report

## Goal

The main goal of our project is to analyze reviews of different gyms in Austin using google map API and Natural Language Processor. As much as we love our beloved Gregory gym on campus, we can't use it once we graduate from this program. So we thought it would be a cool idea to use some of the tools we learned in class and also some new ones to see which gyms in Austin have good reviews and also the reasons behind good ratings. 

## Data
We got data gyms and gyms' google review from "Google API" and "Outscraper".

1. Google API
*	Scrape 60 gym data(google place id, address, latitude, longitude, etc.) from google map API
*	Query(Searching words) **Gym near Travis county**

2. Reviewing data (from Outscraper Website)
* To get review data, we used Outscraper website
* Outscraper(https://outscraper.com/) is the website to get reivews data from google map.
* We pluged google place id that we got above into Outscraper and then we got reviews by each gyms up to 250 recent reviews
The reason why we used outscraper is that we can get only 5 reviews if we use Google API for free.
We paid $10 money to use the outscaper, but you need to pay more money if you want to get more reivews

### Sources

## Analysis



### Methodology
[Procedures]
1. Word count
  * 1.1 All word count
  * 1.2 word count by each places
  * 1.3 word count by each genders
   - We used **NLTK.tokenizer** package to divide each reviews into the tokens(1.1-1.3)
   - Next, we excluded stopwords and additional stopwords in the tokens(1.1-1.3)
   - Counting all of tokens(1.1)
   - Counting all of tokens by each places(1.2)
   - Counting all of tokens by each gender(1.3) with **gender guesser** package

[Packages]
* NLTK: https://www.nltk.org/index.html
* gender guesser: https://pypi.org/project/gender-guesser/

2. Sentiment Analysis
[Procedures]
    * 2.1 Getting sentiment scores(Positive/Negative/Neutral/Compound) by each reviews  
    * 2.2 Mean and Standard Deviation of sentiment scores by each places
    	- We used **NLTK.Vader** package to get sentiment scores by each reviews
  	- We pushed each reviews into vader_analyzer function by NLTK.Vader package and got scores
  	- After that, we also got the mean and the standard deviation of these scores by each places

[Packages]
* NLTK: https://www.nltk.org/_modules/nltk/sentiment/vader.html

### Description and Findings

### Limitations

-	We were able to scrape only 60 gyms. Need to pay for a business license to get more than 60 gyms.
o	Ratings only ranged from 3.5-5. So really bad gyms are not included in the analysis
-	How were these 60 gyms selected? MIGHT BE A QUESTION ASKED
-	Membership price is important, but was not included in our analysis cuz it would be much more complicated of an analysis
-	Regarding gender analysis – possible unknown gender names
-	Some gyms had more than 250 reviews, but 250 was the cap, otherwise we had to pay.


### Extensions

-	More gyms. Maybe not only travis county, but include bigger location.
-	Include membership into our analysis
-	Maybe include recommendation system based on price, what features of the gym you value the most (machine age, price, location, etc)
-	Compare ratings from google map with another party app (ex. Apple map)
-	Yelp has amenities and more section. Maybe run regression to see if we could find any interesting trend between amenities and ratings. (ex. Private parking leads to higher rating?)


### Reproducibility
