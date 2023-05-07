# TMDb_movie_data_analysis
Analyzing TMDb_movie website to answer some questions like explore the correlations between the varies things on it like the popularity and the budget, is the profit is an indicator for the popularity of the movie and is there a corelation between the popularity and votes and who are the top rated directors and actors and so on.

## Questions for Analysis:
* First question after importing and wrangling the data is what is the profit of every film to use it to find the correlations in the coming questions
* Also it is important for me to know the most popular and top rated directors and actors.
* Finally it is important to know the difference between the film production before the 2000s and after 2000s in some questions.

## Data Wrangling section:
* In this section we will do some gathering, assessing and cleaning to the data to be more suatable and easy to analyse.
* After this we know that the data has more than 10K observations and 21 column.
* We know the columns names and data types and the number of the missing data on each one.
  ### Data Cleaning:
  * After gathering the data seems that we have a many missing data on the 'tagline', 'homepage','Keywords' and 'production_companies' columns and we will not use them on our investigation.
  * Finally for cleaning we droped any duplicated values.


## Exploring Data Section:
   > After wrangling the data, In this section we will answer some questions by analysing the data to create some Conclusions about the    dataframe, you can see the analyzing proccess from the <b> ipynb </b>or <b>html</b> files. All these questions is from my deep mind and of course you may have different questions so don't be restricted by this questions.
## Data Visualization Section:
  > After doing the exploration on the data and answering all the questions I took this clean data and put it in [Google data studio](https://lookerstudio.google.com/s/lIxdcCNslrM) to do some visualizing on it and make data easy to read and you can see the interactive report <b> [HERE](https://lookerstudio.google.com/s/lIxdcCNslrM) </b>.
## Conclusion:
* The correlation between the budget and the popularity is 0.54 means if the budget is high that does mean that the movie has chance to be popular.
* The voting results does not return the popularity, because the correlation between them is weak 0.2
* The correlation between the profit and the popularity is a bit strong 0.62 means that the profit shows the popularity.
* Avatar movie makes the biggest revenue ever with 2.7 Billion Dollars.
* The Dark Knight has the highest voting rate as action movie.
* Robert Schwentke has directed 5 movies.
* vin diesel was active every year from 1999 until 2015 except 2007, 2010 and 2012.
* The Godfather is the top rated movie in 70s with 8.3 vote rating.
* Christopher Nolan is the most popular director ever.
* movies revenue had a drop in 2014 but returns stronger in 2015.
* the movies profits has increases after 2000s by about 14M $.
* the movies has limited its length by about 6.8 minutes.
  
  
## DataFrame limitations:
* Of course there's some limitations on this data frame that limited our investigate like the missing data in the production companies column, If this column was clear of missing data we would uses it to investigate more and more in the data frame.
* Also the big amount of 0 values in the budget and revenue columns also affected on our results but generally i think we did great job on this data frame under these limitations.
