# Analytics_Challenge


2020 SCHOLASTICS CHALLENGE DESCRIPTION




Prior to conducting any analyses on the data, a precautionary measure was taken to ensure that no inaccuracies, biases, and misconceptions were present amongst the data. Since the dataset was large (two million records), an SQL database was created to access and query out our inquiries. Data exploration led us to clean the data using Python, and gain valuable insights through the utilization of Tableau. 



Descriptive methods were applied to signal demographic trends among genres, themes, and prices. 25 genres were grouped into 4 unique genre categories: Instructional, Fiction, Media & Miscellaneous, and Non-Fiction. Comparing the average unit price to these genre categories shows that instructional books had the highest average unit price and that the remaining genre groups were relatively similar in terms of pricing. From the 326 themes, 22 theme categories were created, these theme categories reflect the trend, shown by genres, that educational and instructional books were amongst the priciest on average. A visualization with a cluster using the k-means algorithm was produced analyzing the average price of books per state. This visualization shows higher average prices in the southern US with the average price decreasing with northern mobility. 



A significant emphasis was placed on the identification of what the distribution channels were. So, an investigation examining the revenue by individual channels was conducted, and further drilled down into book grade reading levels. The book reading levels (Lexile codes) were extracted from Scholastic’s website to create grade reading level book classifiers. Starting from the 4th-grade reading level, there was an overall decline in revenue between both distribution channels. In support of this, Scholastic’s website highlighted: “The division delivers more than 160,000 fairs in pre-K, elementary, and middle schools across the globe.” These factors helped us conclude that channel 2 seems to exhibit the behaviors of a book fair. This assumption is backed by a near disappearance of revenue from channel 2 after the middle school reading level. The data would also suggest that channel 1 was an online platform, as revenue was spread throughout all reading levels. This insight leads to the recommendation of a selective distribution model involving channel 2 (book fairs) focusing on elementary to middle school book levels, while channel 1 (online) will be used as a general platform for all book levels. 



We formulated a unified strategy for marketing between the two distribution channels. The grade level of books contributing to the lowest source of revenue is 4th-12th grade. One component of our marketing strategy is to create a 30 second Youtube pre-video advertisement to promote and sell to the ages related to 4th-12th grade level books (9-17), as well as parents who have children within that age range. We will create a youtube advertisement, which promotes the scholastic brand across channel 1(internet platform) and channel 2(book fair). We also included user stories to have a deeper understanding of our customer types. We created a cost structure for running youtube pre-video advertisements for one month. The click-through rates & conversion rates are based on industry averages, and the cost of running ads is a function of the viewers of the advertisement. We ended up with a total profit of $515,400 in one month. In addition to pre-video advertisements, we will also be reaching out to influencers who have the highest overlap rate with the scholastic youtube channel audience and securing long term contracts with influencers to lock them in on a set price if their audience increases. Demonetization gives influencers a greater financial incentive to secure contracts with companies. Promoting within the influencers videos leads to a higher click through rate, because of the increasing use of ad-blockers on pre-video advertisements. It also leads to a higher conversion rate, due to the audience's emotional connection to the respective influencer. We also created user stories on influencers to understand who they are and what content they make to match them with the right genres to promote. 



Going forward, Scholastic should attempt to minimize their overlap in their distribution channels by operating in distinct states. Scholastic could use its historical data to create an algorithm based on a book’s characteristics to make a recommendation as to which distribution channel a particular book is more likely to be sold in. A logistic regression model would be perfect because of attempts to predict a binary response, which would best suit Scholastic’s needs by predicting which books could better be sold amongst the two masked distribution channels. In practice, a book would be scanned, a distribution channel would be recommended, and unintentional competition would be prevented. 






