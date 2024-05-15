Research Question: 
Are certain types of advertisements more present in certain times of the year than others? To what extent do advertisers tailor advertisements based on time period versus repeatedly showing the same ads and brands over time? We hypothesize that while we may see some seasonality in the ads that TikTok shows, certain ads and brands will repeatedly appear in users’ video browsing history across all time periods.

Data: 
To investigate the prevalence and characteristics of ads on TikTok, the data we relied on came from data donations from participants who voluntarily shared their account data with us for analysis, and who will be referred to interchangeably as “users.” This data was originally requested and obtained for the purposes of a project investigating the prevalence of news on TikTok and permission has been obtained to employ the same dataset for this study. TikTok allows users to request and receive a JSON file of their own account data through the mobile app, returned to the users as a file called “user_data.json.” These files contain information such as list of followed accounts, video browsing history, and other features including sensitive information. Some user file requests return a file without any video browsing history; in total, across many user requests, we conducted our analysis on the 9 files containing video browsing history for this study.

In order to protect user privacy, we ran each user_data.json file through a Python script that extracted only the video browsing history without other identifying information. All 9 of these raw data files were named with a 5-digit code to be referred to anonymously throughout the study. The 9 codes were: 10824, 12345, 26301, 33534, 38129, 50405, 74721, 77217, 77777. 

To extract the video metadata into .csv files for ease of analysis, we used a modified version of the Pyktok library, a module that retrieves metadata from TikTok videos, including variables such as author, description, hashtags, etc. One active bot was employed per user, using functions from the modified PykTok.py Class. The modified class 1.) no longer saves a video when a video is not flagged, 2.) does not stop execution when a video is missing, and 3.) adds a new column ‘suggested_words’ containing more textual content about a video which may be useful for analysis. Active bots were executed through terminal Pyktok commands on several computers. When initiated, each bot would begin to populate a .csv file named results_nnnnn.csv with the metadata of each video appearing in the user’s browsing history, with nnnnn being the user code. After successfully collecting metadata on all the videos in the raw data file, the program would terminate. All subsequent analyses to investigate the prevalence and characteristics of ads on Tiktok were done using the data contained within the results_nnnnn.csv files. 



Methods:
In our first research question, we aim to discover if there is a relationship between the type of advertisement and the time of year. To answer this question, we perform analyses on several different characteristics of the donated data to identify the prevalence of certain topics during different times of the year. We must identify a set of topics common to our pool of ads, label each video with a topic, and then plot the prevalence of these topics over a time period. To identify a set of topics for the advertisements, we use topic modeling, specifically the Latent Dirichlet allocation (LDA) model. The donated data includes an indication for whether a video is an ad, the video creation date, and various descriptive features of a video. Each video is treated as a document using the fields of suggested words, author username, and caption. Running the LDA algorithm, we make a reasonable list of broad advertisement categories. We sort the videos and categories by user to ensure ease of analysis to aid in answering our second research question, but for this research question we look at all the categories for all users together, differentiating by time of year instead of by user. To identify the prevalence of advertisement topics at different times of the year, first we identify the time period that each user’s data spans. Then for each topic, we plot the number of documents that appear each month, for the amount of time spanned. We then are able to identify whether there seems to be changes in topics that surround major seasons or events.


Data
1. Folder: user_jsons - holds the raw user json files of the donated data
2. Folder: pyktok_data - holds the donated raw data collected with Pyktok from the Json files
3. Folder: user_jsons_tospli -  json files that were split for more data collection from the raw json files (pyktok_data did not include a full collection of all the user jsons)

Processing Data
4. File: CompleteDateTime - Initial way of merging the raw json files and Pyktok data from each json file, specifically the data watched (only worked for three files, may be due to differences in gathering data in the groups that donated data)
5. Folder: merged datasets
    6. File: Merging Datasets: final way of merging json and csv files used to create
    7. Files: Merged user json/csv into a csv file for each user where we had access to both raw files, using 6.
    8. Folder: Additional collecting - the data from additional collections of data from the json files (that were not collected before)
9. File: looking_at_jsons - some exploration of files to find out features before processing (all the processing previously listed)

10. File: ad_exploration - initial exploration of the data (time period, ad precense, what ads, etc.) to guide further research
11. File: Ads Topic Modeling/topic_modeling - topic modeling performed on the ads available to try and extrapolate possible general topic groups in the ads
12. Folder: visualizations - images of the visualiations created from exploration
13. Zip: cs315project... - Pyktok collection method that was run