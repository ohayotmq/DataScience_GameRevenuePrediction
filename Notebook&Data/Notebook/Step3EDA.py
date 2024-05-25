
def Step3EDA():
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        
        df = pd.read_csv("../Data/game_info_cleaned.csv")
        df.head()

        df.describe()

        df.columns

        pd.crosstab(index=df['Genre'], columns='count').sort_values('count',ascending=False)

        pd.crosstab(index=df['Console'], columns='count').sort_values('count', ascending=False)

        pd.crosstab(index=df['Release Year'], columns='count')

        pd.crosstab(index=df['Publisher'], columns='count').sort_values('count', ascending=False)

        sns.set_style("white")
        plt.figure(figsize = (8,6))
        plt.hist(df["Total Sales (m)"],
                bins = 14,
                color = "#108a99")
        plt.title("Distribution of Total Sales", fontsize = 14, weight = "bold")
        plt.xlabel("Total Sales (m)")
        plt.ylabel("Number of Titles")
        sns.despine()

        plt.savefig("../Figure/EDA/TotalSalesHistogram.png")
        #plt.show()


        sns.set_style("white")
        plt.figure(figsize = (8,6))
        plt.hist(df["NA Sales (m)"],
                bins = 14,
                color = "#108a99")
        plt.title("Distribution of NA Sales", fontsize = 14, weight = "bold")
        plt.xlabel("NA Sales (m)")
        plt.ylabel("Number of Titles")
        sns.despine()
        plt.savefig("../Figure/EDA/NASalesHistogram.png")
        #plt.show()

        sns.set_style("white")
        plt.figure(figsize = (8,6))
        plt.hist(df["EU Sales (m)"],
                bins = 14,
                color = "#108a99")
        plt.title("Distribution of EU Sales", fontsize = 14, weight = "bold")
        plt.xlabel("EU Sales (m)")
        plt.ylabel("Number of Titles")
        sns.despine()
        plt.savefig("../Figure/EDA/EUSalesHistogram.png")
        #plt.show()


        sns.set_style("white")
        plt.figure(figsize = (8,6))
        plt.hist(df["JP Sales (m)"],
                bins = 14,
                color = "#108a99")
        plt.title("Distribution of JP Sales", fontsize = 14, weight = "bold")
        plt.xlabel("JP Sales (m)")
        plt.ylabel("Number of Titles")
        sns.despine()
        plt.savefig("../Figure/EDA/JPSalesHistogram.png")
        #plt.show()

        sns.set_style("white")
        plt.figure(figsize = (8,6))
        plt.hist(df["Other Sales (m)"],
                bins = 14,
                color = "#108a99")
        plt.title("Distribution of Other Sales", fontsize = 14, weight = "bold")
        plt.xlabel("Other Sales (m)")
        plt.ylabel("Number of Titles")
        sns.despine()
        plt.savefig("../Figure/EDA/OtherSalesHistogram.png")
        #plt.show()

        gen_df = df.groupby(['Genre'], as_index=False)['Total Sales (m)'].sum().sort_values('Total Sales (m)', ascending=False)
        gen_df = gen_df.reset_index(drop=True)
        gen_df

        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.bar(x = gen_df['Genre'], 
                height = gen_df["Total Sales (m)"],
                color = my_colors,
                edgecolor = 'black')
        plt.xticks(rotation = 85, fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Total Sales(m) by Genre", fontsize = 16, fontweight = "bold")
        plt.ylabel("Total Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/TotalSalesByGenre.png")
        #plt.show()


        con_df = df.groupby(['Console'], as_index=False)['Total Sales (m)'].sum().sort_values('Total Sales (m)', ascending=False)
        con_df = con_df.reset_index(drop=True)
        con_df


        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.bar(x = con_df["Console"], 
                height = con_df["Total Sales (m)"],
                color = my_colors,
                edgecolor = 'Black')
        plt.xticks(rotation = 85, fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Total Sales(m) by Console", fontsize = 16, fontweight = "bold")
        plt.ylabel("Total Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/TotalSalesByConsole.png")
        #plt.show()

        pub_df = df.groupby(['Publisher'], as_index=False)['Total Sales (m)'].sum().sort_values('Total Sales (m)', ascending=False)[:20]
        pub_df = pub_df.reset_index(drop=True)
        pub_df


        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.bar(x =  pub_df['Publisher'], 
                height = pub_df["Total Sales (m)"],
                color = my_colors,
                edgecolor = 'black')
        plt.xticks(rotation = 85, fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Total Sales by Publisher (Top 20) ", fontsize = 16, fontweight = "bold")
        plt.ylabel("Total Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/TotalSalesByPublisher20.png")
        #plt.show()

        bsgw_df = df.groupby(['Title'], as_index=False)['Total Sales (m)'].sum().sort_values('Total Sales (m)', ascending=False)[:10]
        bsgw_df = bsgw_df.reset_index(drop=True).sort_values('Total Sales (m)', ascending=True)
        bsgw_df


        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.barh(y =  bsgw_df['Title'], 
                width = bsgw_df["Total Sales (m)"],
                color = my_colors,
                edgecolor = 'black')
        plt.xticks(fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Top 10 Best Selling Games Worldwide", fontsize = 16, fontweight = "bold")
        plt.xlabel("Total Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/Top10BestSellingGames.png")
        #plt.show()


        bsgna_df = df.groupby(['Title'], as_index=False)['NA Sales (m)'].sum().sort_values('NA Sales (m)', ascending=False)[:10]
        bsgna_df = bsgna_df.reset_index(drop=True).sort_values('NA Sales (m)', ascending=True)
        bsgna_df

        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.barh(y =  bsgna_df['Title'], 
                width = bsgna_df["NA Sales (m)"],
                color = my_colors,
                edgecolor = 'black')
        plt.xticks(fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Top 10 Best Selling Games NA", fontsize = 16, fontweight = "bold")
        plt.xlabel("NA Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/Top10BestSellingGamesNA.png")
        #plt.show()

        bsgeu_df = df.groupby(['Title'], as_index=False)['EU Sales (m)'].sum().sort_values('EU Sales (m)', ascending=False)[:10]
        bsgeu_df = bsgeu_df.reset_index(drop=True).sort_values('EU Sales (m)', ascending=True)
        bsgeu_df

        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.barh(y =  bsgeu_df['Title'], 
                width = bsgeu_df["EU Sales (m)"],
                color = my_colors,
                edgecolor = 'black')
        plt.xticks(fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Top 10 Best Selling Games EU", fontsize = 16, fontweight = "bold")
        plt.xlabel("EU Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/Top10BestSellingGamesEU.png")
        #plt.show()

        bsgjp_df = df.groupby(['Title'], as_index=False)['JP Sales (m)'].sum().sort_values('JP Sales (m)', ascending=False)[:10]
        bsgjp_df = bsgjp_df.reset_index(drop=True).sort_values('JP Sales (m)', ascending=True)
        bsgjp_df

        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.barh(y =  bsgjp_df['Title'], 
                width = bsgjp_df["JP Sales (m)"],
                color = my_colors,
                edgecolor = 'black')
        plt.xticks(fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Top 10 Best Selling Games JP", fontsize = 16, fontweight = "bold")
        plt.xlabel("JP Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/Top10BestSellingGamesJP.png")
        #plt.show()

        bsgot_df = df.groupby(['Title'], as_index=False)['Other Sales (m)'].sum().sort_values('Other Sales (m)', ascending=False)[:10]
        bsgot_df = bsgot_df.reset_index(drop=True).sort_values('Other Sales (m)', ascending=True)
        bsgot_df

        my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        plt.figure(figsize =(12,9))
        plt.barh(y =  bsgot_df['Title'], 
                width = bsgot_df["Other Sales (m)"],
                color = my_colors,
                edgecolor = 'black')
        plt.xticks(fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Top 10 Best Selling Games Other", fontsize = 16, fontweight = "bold")
        plt.xlabel("Other Sales(m)", fontsize = 13)
        plt.savefig("../Figure/EDA/Top10BestSellingGamesOther.png")
        #plt.show()






        import numpy as np
        yearly_sales_df = df.groupby(['Release Year'], as_index=False).agg({'Total Sales (m)': 'sum',
                                                                        'NA Sales (m)': 'sum',
                                                                        'EU Sales (m)': 'sum',
                                                                        'JP Sales (m)': 'sum',
                                                                        'Other Sales (m)': 'sum'})

        #Dropped the year 1970 as there is a tremendous gap between 70-78 with no data
        yearly_sales_df = yearly_sales_df.drop([0,1])

        yearly_sales_df = yearly_sales_df.reset_index(drop=True)
        yearly_sales_df


        labels = ["Total", "NA", "EU", "JP", "Other"]
        plt.figure(figsize = (20,14))
        plt.plot(yearly_sales_df["Release Year"], yearly_sales_df["Total Sales (m)"], color = "#173F5F")
        plt.plot(yearly_sales_df["Release Year"], yearly_sales_df["NA Sales (m)"], color = "#20639B")
        plt.plot(yearly_sales_df["Release Year"], yearly_sales_df["EU Sales (m)"], color = "#3CAEA3")
        plt.plot(yearly_sales_df["Release Year"], yearly_sales_df["JP Sales (m)"], color = "#F6D55C")
        plt.plot(yearly_sales_df["Release Year"], yearly_sales_df["Other Sales (m)"], color = "#ED553B")
        plt.title("Sales over Time (1978-2020)", fontsize = 16, fontweight = "bold")
        plt.ylabel("Sales (m)", fontsize = 15)
        plt.yticks(fontsize = 13)
        plt.xlabel("Release Year", fontsize = 15)
        plt.xticks(yearly_sales_df["Release Year"], rotation = 45, fontsize = 13)
        plt.legend(labels = labels, fontsize = "large")
        plt.savefig("../Figure/EDA/TotalSalesOverTime.png")
        #plt.show()



        genre_cgsales_df = df.groupby(['Genre'], as_index=False).agg({'Total Sales (m)': 'sum',
                                                                        'NA Sales (m)': 'sum',
                                                                        'EU Sales (m)': 'sum',
                                                                        'JP Sales (m)': 'sum',
                                                                        'Other Sales (m)': 'sum'})

        genre_cgsales_df = genre_cgsales_df.sort_values('Total Sales (m)', ascending=False)
        genre_cgsales_df = genre_cgsales_df.reset_index(drop=True)
        genre_cgsales_df


        #my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        labels = ["NA", "EU", "JP", "Other"]
        plt.figure(figsize =(12,9))

        bars1 = np.add(genre_cgsales_df["NA Sales (m)"], genre_cgsales_df["EU Sales (m)"]).tolist()
        bars2 = np.add(genre_cgsales_df["JP Sales (m)"], bars1).tolist()

        p1 = plt.bar(x = genre_cgsales_df['Genre'], 
                height = genre_cgsales_df["NA Sales (m)"],
                color = '#ED553B',
                edgecolor = 'black')

        p2 = plt.bar(x = genre_cgsales_df['Genre'],
                bottom = genre_cgsales_df["NA Sales (m)"],
                height = genre_cgsales_df["EU Sales (m)"],
                color = '#F6D55C',
                edgecolor = 'black')

        p3 = plt.bar(x =genre_cgsales_df['Genre'], 
                bottom = bars1,
                height = genre_cgsales_df["JP Sales (m)"],
                color = '#3CAEA3',
                edgecolor = 'black')

        p4 = plt.bar(x =genre_cgsales_df['Genre'],
                bottom = bars2,
                height = genre_cgsales_df["Other Sales (m)"],
                color = '#20639B',
                edgecolor = 'black')

        plt.xticks(rotation = 85, fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Total Sales by Genre by Country Grouping ", fontsize = 16, fontweight = "bold")
        plt.ylabel("Total Sales(m)", fontsize = 13)
        plt.legend(labels = labels, fontsize = "large")
        plt.savefig("../Figure/EDA/TotalSalesByGenreByCG.png")
        #plt.show()


        console_cgsales_df = df.groupby(['Console'], as_index=False).agg({'Total Sales (m)': 'sum',
                                                                        'NA Sales (m)': 'sum',
                                                                        'EU Sales (m)': 'sum',
                                                                        'JP Sales (m)': 'sum',
                                                                        'Other Sales (m)': 'sum'})

        console_cgsales_df = console_cgsales_df.sort_values('Total Sales (m)', ascending=False)
        console_cgsales_df = console_cgsales_df.reset_index(drop=True)
        console_cgsales_df

        #my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        labels = ["NA", "EU", "JP", "Other"]
        plt.figure(figsize =(12,9))

        bars1 = np.add(console_cgsales_df["NA Sales (m)"], console_cgsales_df["EU Sales (m)"]).tolist()
        bars2 = np.add(console_cgsales_df["JP Sales (m)"], bars1).tolist()

        p1 = plt.bar(x = console_cgsales_df['Console'], 
                height = console_cgsales_df["NA Sales (m)"],
                color = '#ED553B',
                edgecolor = 'black')

        p2 = plt.bar(x = console_cgsales_df['Console'],
                bottom = console_cgsales_df["NA Sales (m)"],
                height = console_cgsales_df["EU Sales (m)"],
                color = '#F6D55C',
                edgecolor = 'black')

        p3 = plt.bar(x = console_cgsales_df['Console'], 
                bottom = bars1,
                height = console_cgsales_df["JP Sales (m)"],
                color = '#3CAEA3',
                edgecolor = 'black')

        p4 = plt.bar(x = console_cgsales_df['Console'],
                bottom = bars2,
                height = console_cgsales_df["Other Sales (m)"],
                color = '#20639B',
                edgecolor = 'black')

        plt.xticks(rotation = 85, fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Total Sales by Console by Country Grouping ", fontsize = 16, fontweight = "bold")
        plt.ylabel("Total Sales(m)", fontsize = 13)
        plt.legend(labels = labels, fontsize = "large")
        plt.savefig("../Figure/EDA/TotalSalesByConsoleByCG.png")
        #plt.show()

        publisher_cgsales_df = df.groupby(['Publisher'], as_index=False).agg({'Total Sales (m)': 'sum',
                                                                        'NA Sales (m)': 'sum',
                                                                        'EU Sales (m)': 'sum',
                                                                        'JP Sales (m)': 'sum',
                                                                        'Other Sales (m)': 'sum'})

        publisher_cgsales_df = publisher_cgsales_df.sort_values('Total Sales (m)', ascending=False)[:20]
        publisher_cgsales_df = publisher_cgsales_df.reset_index(drop=True)
        publisher_cgsales_df


        #my_colors = ('#173F5F', '#20639B', '#3CAEA3', '#F6D55C', '#ED553B')
        labels = ["NA", "EU", "JP", "Other"]
        plt.figure(figsize =(12,9))

        bars1 = np.add(publisher_cgsales_df["NA Sales (m)"], publisher_cgsales_df["EU Sales (m)"]).tolist()
        bars2 = np.add(publisher_cgsales_df["JP Sales (m)"], bars1).tolist()

        p1 = plt.bar(x = publisher_cgsales_df['Publisher'], 
                height = publisher_cgsales_df["NA Sales (m)"],
                color = '#ED553B',
                edgecolor = 'black')

        p2 = plt.bar(x = publisher_cgsales_df['Publisher'],
                bottom = publisher_cgsales_df["NA Sales (m)"],
                height = publisher_cgsales_df["EU Sales (m)"],
                color = '#F6D55C',
                edgecolor = 'black')

        p3 = plt.bar(x = publisher_cgsales_df['Publisher'], 
                bottom = bars1,
                height = publisher_cgsales_df["JP Sales (m)"],
                color = '#3CAEA3',
                edgecolor = 'black')

        p4 = plt.bar(x = publisher_cgsales_df['Publisher'],
                bottom = bars2,
                height = publisher_cgsales_df["Other Sales (m)"],
                color = '#20639B',
                edgecolor = 'black')

        plt.xticks(rotation = 85, fontsize = 13)
        plt.yticks(fontsize = 13)
        plt.title("Total Sales by Publisher by Country Grouping ", fontsize = 16, fontweight = "bold")
        plt.ylabel("Total Sales(m)", fontsize = 13)
        plt.legend(labels = labels, fontsize = "large")
        plt.savefig("../Figure/EDA/TotalSalesByPublisherByCG.png")
        #plt.show()

        print("Done Step3 EDA")




#Call file step chạy bằng câu gọi hàm bên dưới
#Step3EDA()