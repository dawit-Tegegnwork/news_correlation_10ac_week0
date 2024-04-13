<<<<<<< HEAD

### Some of the functions available in the notebooks and codes in this repository

#### Slack Data Parsing Functions
`slack_parser`: Parses Slack data to extract relevant information such as message type, content, sender details, thread information, etc. Combines data from multiple JSON files and returns a DataFrame.

`parse_slack_reaction`: Retrieves reaction-related information from Slack data, including reaction name, count, users, associated message, and user ID. Returns a DataFrame.

`convert_2_timestamp`: Converts Unix time to a readable timestamp for specified columns in the DataFrame.

#### User Interaction and Community Analysis Functions
`get_tagged_users`: Extracts all user mentions (@) from messages.

`get_community_participation`: Analyzes community participation by counting the number of replies for each user.

`map_userid_2_realname`: Maps Slack IDs to real names using user profiles. Optionally, plots a bar graph of message counts for each user.

`get_top_20_user`: Plots the top 20 message senders in a specified channel.

`draw_avg_reply_count`: Plots the average number of reply counts per sender in a channel.

`draw_avg_reply_users_count`: Plots the average number of reply user counts per sender in a channel.

`draw_wordcloud`: Generates and displays a word cloud visualization for message content.

`draw_user_reaction`: Plots users with the most reactions in a channel.

#### Data Analysis and Visualization
`get_top_20_user(dfall_week, channel='All learning')`: Visualizes the top 20 message senders.

`draw_avg_reply_count(dfall_week, channel='All Learning')`: Visualizes the average reply count per sender.

`draw_avg_reply_users_count(dfall_week, channel='All learning')`: Visualizes the average reply user count per sender.

`draw_wordcloud(dfall_week['msg_content'], week='All Learning Week')`: Displays a word cloud for message content.

`draw_user_reaction`: Plots users with the most reactions.

=======
# News Analysis EDA

This code performs Exploratory Data Analysis (EDA) on a news dataset to answer the following questions:

1. **Who are the top and bottom 10 Websites that have the largest count of news articles?**
2. **Analyzing and visualizing websites with the highest numbers of visitor traffic.**
3. **Countries with the highest number of news media organizations (represented by domains in the data).**
4. **Countries that have many articles written about them - the content of the news is about that country.**
5. **Websites that reported (the news content) about Africa, US, China, EU, Russia, Ukraine, Middle East?**

## Prerequisites

- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## Installation

1. Clone the repository or download the code files.
2. Install the required packages using pip:

```
pip install pandas matplotlib seaborn
```

## Usage

1. Ensure that the necessary datasets (`data.csv`, `domains_location.csv`, and `traffic_data.csv`) are available in the same directory as the code.
2. Run the code in a Python environment.

## Code Explanation

1. **Task 1.A**: The code groups the news articles by their source websites and counts the number of articles for each website. It then displays the top 10 and bottom 10 websites with the most and least articles, respectively.

2. **Task 1.B**: The code sorts the `traffic_data` dataset by the `GlobalRank` column in descending order to get the top websites with the highest traffic. It then visualizes the top 10 websites using a bar plot.

3. **Task 1.C**: The code counts the number of news media organizations (represented by domains) for each country and displays the top 10 countries with the most news media organizations. It then visualizes the results using a bar plot.

4. **Task 1.D**: The code iterates through the news articles, searching for the presence of predefined country names in the title and description of each article. It then counts the frequency of each country and displays the top 10 countries with the most articles written about them.

5. **Task 1.E**: The code defines a mapping of countries to their respective regions (continents) and then iterates through the news articles, checking for mentions of the countries and mapping them to their corresponding regions. It then counts the number of articles related to each region and displays the results.

## Limitations and Improvements

- The code assumes that the predefined country-to-region mapping is comprehensive and accurate. In a real-world scenario, this mapping would need to be more robust and handle edge cases.
- The code could be further improved by incorporating additional analysis, such as sentiment analysis, topic modeling, or named entity recognition, to gain deeper insights into the news content.
- The code could be made more modular and reusable by separating the different tasks into distinct functions or modules.
- Error handling and input validation could be added to make the code more robust and user-friendly.

## Conclusion

This code provides a comprehensive EDA on a news dataset, allowing you to gain insights into the top websites, website traffic, news media organization distribution, and the countries that are the focus of news coverage. The results can be used to inform strategic decision-making, content planning, and audience targeting for news organizations or media-related businesses.
>>>>>>> d7d2ed8c2e2caa5623e6ba005570615c4f6517fd
