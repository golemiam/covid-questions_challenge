import csv
import pandas as pd

def main():
    """
    Main program for addressing challenge questions
    :return:
    Returns values based on user input
    """

    run_project()
def run_project():
    """
    Chooses a question to address
    :return:
    Returns the function chosen.
    """
    pd.set_option('display.max_columns', 22)
    question_choice = input("Which question would you like to run? ")
    if question_choice == "1":
        read_panda_file_question_1()
    elif question_choice == "2":
        read_panda_file_question_2()
    elif question_choice == "3":
        pass
    elif question_choice == "4":
        pass
    elif question_choice == "t":
        test()

def test():
    """
    This is my testing ground for my certificate practice.

    Scroll to line 155 (date 4/11/2023 will change)
    :return:
    Depends on what I'm practicing.
    """
    df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    #print(df.head(11))
    #print(df.head(0))
    #print(df.shape)
    #print(df.info())
    #print(df.describe(include="object"))
    #print(df['Residents Weekly Confirmed COVID-19'].value_counts().plot(kind="bar"))
    mnt_fruits = []
    for i in range(len(df)):
        mnt_fruits.append(i)
    #print(mnt_fruits)
    new_df = df[
        [
            'Week Ending',
            'Residents Weekly Confirmed COVID-19'
        ]
    ]
    #print(new_df[2114:7447])
    #print(df.loc[2114:7446, 'Week Ending': 'Residents Weekly Confirmed COVID-19'])
    #print(df.iloc[1:9:2, -5:-1])
    #print(df['Residents Weekly Confirmed COVID-19'].interpolate())
    #print(df[-df['Residents Weekly Confirmed COVID-19'].isnull()])

    #df_no_null = df.fillna(0)
    #print(df_no_null[df_no_null['Residents Weekly Confirmed COVID-19'].isnull()])

    time_df = pd.to_datetime(df['Week Ending'])
    month = time_df.dt.month
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.show()
    #print(month)
    #print(sns.histplot(month.head(12), kde=False, bins=12))
    def day_vs_night(self):
        daytime = ''
        if self < 1:
            daytime = 'Not Known'
        elif self < 4:
            daytime = 'Morning'
        elif self < 7:
            daytime = 'Afternoon'
        elif self < 10:
            daytime = 'Evening'
        elif self >= 10:
            daytime = 'Night Time'
        return daytime
    #print(month.apply(day_vs_night))
    high_covid = df[df['Residents Weekly Confirmed COVID-19'] > 4]
    #print(high_covid)
    vacced_more_than_zero = df[df['Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time'] > 0]
    #print(vacced_more_than_zero)
    ##both_fulfilled = [df[df['Residents Weekly Confirmed COVID-19'] > 4] & df[df['Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time'] > 0]]
    #print(both_fulfilled.dtypes)
    #print(vacced_more_than_zero['Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time'].dtypes)
    #print(df.loc[df['Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time'] > 0, 'vacced_more_than_zero'] = 'some_vacc')
    added_column = df.loc[df['Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time'] == 0, 'vacced_more_than_zero'] = 'none_vacc'
    #print(added_column)
    cdf = df.rename(columns={
        'Week Ending': 'W_End',
        'Federal Provider Number': 'FP_num',
        'Provider Name': 'P_name',
        'Provider City': 'P_city',
        'Provider State': 'P_state',
        'Provider Zip Code': 'P_zip',
        'Provider Phone Number': 'P_Phone_#',
        'Residents Weekly Confirmed COVID-19': 'Cov_residents',
        'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time': 'HCP#_vacc',
        'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_1',
        'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_2',
        'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_3',
        'Number of Healthcare Personnel with a Completed Vaccination Eligible to Work in this Facility for At Least 1 Day This Week who Received a COVID-19 Vaccine Booster at Any Time': 'HCP#_2',
        'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_4',
        'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_5',
        'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_6',
        'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_7',
        'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines': 'Percentage_8'
    })
    # 3 columns 3 conditions
    # P_state = Utah
    # Cov_residents > 1
    # Percentage_7 > 80
    #print(cdf.loc[cdf['P_state'] == 'UT' & (cdf['Cov_residents'] > 1)])
    #print(cdf.loc[cdf['Cov_residents'] > 1 & (cdf['Percentage_7'] > 80) & (cdf['Percentage_8'] > 80) & (cdf['P_state'] == 'UT')])
    plus_res = cdf['Cov_residents'] > 1
    plus_7 = cdf['Percentage_7'] > 80
    plus_8 = cdf['Percentage_8'] > 80
    combined = (-(plus_res & plus_7 & plus_8))
    #print(combined.head(40))

    #print(cdf.groupby('Percentage_8').head().mean())[combined]
    #print(cdf.mean(cdf['Percentage_8']))

    def add_5():
        a = 0
        a + 5
        return a
    #print(cdf.groupby(['Percentage_7', 'FP_num'])['Cov_residents'].agg(['median', 'max']).sort_values('max', ascending = False).head(5))
    def max_5(self):
        cdf.groupby(['Percentage_7', 'FP_num'])['Cov_residents'].agg(['median', 'max']).sort_values('max', ascending=False).head(5)
    #print(cdf.apply(max_5))
    #pct = cdf.pct_change()
    #print(pct)
    #divider = df['Percentage_7']
    #print(divider)
    cdf['quotient'] = cdf['Cov_residents']/month
    #print(cdf['Cov_residents'].head(10))
    #print(cdf)
    #print(cdf['Cov_residents'])
    covid_zero = cdf[cdf.Cov_residents == 0]
    print(covid_zero.columns.get_loc['Cov_residents'])
    #print(covid_zero)
    #cdf['counter'] = cdf[cdf['Cov_residents'] == 0]
    #print(cdf.info)



def read_panda_file_question_1():
    """
    This function is used to collect the data, get user input, and give a response based on input.
    The input request gives the details.
    :return:
    Returns percentage values over 80% for the various percentage columns for healthcare personnel.
    """
    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    covid_simple_titles = covid_df.rename(columns= {
    'Week Ending': 'W_End', 
    'Federal Provider Number': 'FP_num', 
    'Provider Name': 'P_name', 
    'Provider City': 'P_city', 
    'Provider State': 'P_state', 
    'Provider Zip Code': 'P_zip', 
    'Provider Phone Number': 'P_Phone_#', 
    'Residents Weekly Confirmed COVID-19': 'Cov_residents', 
    'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time': 'HCP#_vacc', 
    'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_1', 
    'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_2', 
    'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_3', 
    'Number of Healthcare Personnel with a Completed Vaccination Eligible to Work in this Facility for At Least 1 Day This Week who Received a COVID-19 Vaccine Booster at Any Time': 'HCP#_2', 
    'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_4', 
    'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_5', 
    'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_6', 
    'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_7', 
    'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines': 'Percentage_8'
    })
    print(covid_simple_titles.info())
    user_choice = input("""Which Percentage information would you like? 
    A for 'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time' 
    B for 'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time'
    C for 'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time'
    D for 'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time'
    E for 'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time'
    F for 'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines'
    G for 'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines'
    H for 'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines'
    """)
    if user_choice == 'A'.lower():
        #
        percent = covid_simple_titles.Percentage_1[(covid_simple_titles.Percentage_1>80)]
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_1 > 80]

        print(f"{percent_a['W_End']} : {percent_a['Percentage_1']}")
    if user_choice == 'B'.lower():
        print(covid_simple_titles.Percentage_2[(covid_simple_titles.Percentage_2 > 80)])
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_2 > 80]
        print(f"{percent_a['W_End']} : {percent_a['Percentage_2']}")

    if user_choice == 'C'.lower():
        print(covid_simple_titles.Percentage_3[(covid_simple_titles.Percentage_3 > 80)])
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_3 > 80]
        print(f"{percent_a['W_End']} : {percent_a['Percentage_3']}")
    if user_choice == 'D'.lower():
        print(covid_simple_titles.Percentage_4[(covid_simple_titles.Percentage_4 > 80)])
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_4 > 80]
        print(f"{percent_a['W_End']} : {percent_a['Percentage_4']}")
    if user_choice == 'E'.lower():
        print(covid_simple_titles.Percentage_5[(covid_simple_titles.Percentage_5 > 80)])
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_5 > 80]
        print(f"{percent_a['W_End']} : {percent_a['Percentage_5']}")
    if user_choice == 'F'.lower():
        print(covid_simple_titles.Percentage_6[(covid_simple_titles.Percentage_6 > 80)])
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_6 > 80]
        print(f"{percent_a['W_End']} : {percent_a['Percentage_6']}")
    if user_choice == 'G'.lower():
        print(covid_simple_titles.Percentage_7[(covid_simple_titles.Percentage_7 > 80)])
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_7 > 80]
        print(f"{percent_a['W_End']} : {percent_a['Percentage_7']}")
    if user_choice == 'H'.lower():
        #print(covid_simple_titles.Percentage_8[(covid_simple_titles.Percentage_8 > 80)])
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_8 > 80]
        print(f"Week: {percent_a['W_End']} : Percent: {percent_a['Percentage_8']}")
    print(covid_df.info())

def read_panda_file_question_2():
    """
    Helps answer the question regarding the longest streak of residents not testing
    positive for covid.
    :return:
    returns the value of the longest streaks.
    """
    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    covid_simple_titles = covid_df.rename(columns={
        'Week Ending': 'W_End',
        'Federal Provider Number': 'FP_num',
        'Provider Name': 'P_name',
        'Provider City': 'P_city',
        'Provider State': 'P_state',
        'Provider Zip Code': 'P_zip',
        'Provider Phone Number': 'P_Phone_#',
        'Residents Weekly Confirmed COVID-19': 'covid_weekly_count',
        'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time': 'HCP#_vacc',
        'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_1',
        'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_2',
        'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_3',
        'Number of Healthcare Personnel with a Completed Vaccination Eligible to Work in this Facility for At Least 1 Day This Week who Received a COVID-19 Vaccine Booster at Any Time': 'HCP#_2',
        'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_4',
        'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_5',
        'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_6',
        'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_7',
        'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines': 'Percentage_8'
    })
    print(covid_simple_titles['covid_weekly_count'])
    covid_simple_titles.groupby(['covid_weekly_count']).size()
    week_index = covid_simple_titles.set_index('W_End')
    #print(week_index)
    zeros = week_index[week_index['covid_weekly_count'] == 0]
    #print(covid_simple_titles['covid_weekly_count'].head(20))
    print(covid_simple_titles['W_End'].head(20))
    print(zeros['covid_weekly_count'].head(20))
    print(zeros['covid_weekly_count'].count())
    print(covid_simple_titles['W_End'].count())
    """
    for covid_weekly_count,group in covid_simple_titles.groupby('covid_weekly_count'):
        print(group)
    count = []
    for i in range(0, len(covid_simple_titles)):
        count = covid_simple_titles['covid_weekly_count'] == 0
        streak = count + 1
        count_column.append(streak)
    
    """
    covid_count = covid_simple_titles['covid_weekly_count']
    def counter(self, counted):
        counting = 0
        counted = 0
        if self < 1:
            counted = counted + 1
            return counted
        if self >= 1:
            counting = 0
        return counted
    print(covid_count.apply(counter))

    #print(month.apply(day_vs_night))

if __name__ == "__main__":
    main()
