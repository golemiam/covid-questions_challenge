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
        read_panda_file_question_3()
    elif question_choice == "4":
        pass




def read_panda_file_question_1():
    """
    This function is used to collect the data, get user input, and give a response based on input.
    The input request gives the details.
    :return:
    Returns percentage values over 80% for the various percentage columns for healthcare personnel.
    """
    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    provider_df = pd.read_csv('Our_Provider_numbers.csv')
    #converts csv to a variable for use.

    facility_choice = input("""
       Which facility would you like information for? '1' for everything, '2' for everything at ensign. For 
       everything else name the facility you would like listed.
       """)
    if facility_choice == '1'.lower():
        pass
    elif facility_choice == '2'.lower():
        provider_df = pd.read_csv("Our_Provider_numbers.csv")
        provider_simple_title = provider_df.rename(columns={
            "our affilitied federal provider numbers": "Provider Numbers"
        })
        #print(provider_df.head(3))


        combo_df = pd.concat(objs= [covid_df, provider_simple_title])
        #combo_df = combo_df.dropna(subset= ["Provider Numbers"])
        #print(combo_df)
        #print(combo_df.head(1))
        #mask = combo_df["Federal Provider Number"].isin(combo_df["Provider Numbers"])
        #print(combo_df[mask])
        #print(provider_series.head(3))
        provider_numbers = provider_simple_title["Provider Numbers"]
        #print(provider_numbers.head(3))
        provider_names = covid_df["Provider Name"]
        covid_grouped = covid_df.groupby("Provider Name")
        #print(covid_grouped.head(3))
        provider_index_df = pd.read_csv("COVID_19_Nursing_Home_Data_01_22_2023.csv", index_col="Federal Provider Number")
        #print(provider_index_df.head(3))
        covid_grouped = provider_index_df.groupby("Provider Name")
        #print(covid_grouped["Provider Name"].head(3))
        mask = covid_df["Provider Name"] == "THE LODGE OF SAGINAW HEALTH AND WELLNESS"
        #print(covid_df[mask])

        #covid_df["Provider Numbers"] = provider_df
        #print(covid_df["Provider Numbers"].head(3))
        #mask = covid_df["Federal Provider Number"].isin(provider_numbers)
        #print(mask.head(3))
        unstacked_df = combo_df.unstack()
        print(unstacked_df.head(40000000))

        for row, covid_df['Federal Provider Number'] in zip(provider_df, covid_df):
            provider_df = covid_df['Provider Name']
        print(provider_df.info())
        provider_set = provider_df
        #print(provider_df[provider_set])
        repeated_list = []
        for row in zip(provider_df, provider_set):
            if provider_df[row].is_unique():
                provider_set.append(row[1])
                print(1)
            else:
                print("nope")

    #print(provider_set)

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
    #Changes column names for easier calculations




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
    # prompts the user for a selection
    if user_choice == 'A'.lower():
        #Uses selection A
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_1 > 80]
        # Collects over 80 percent values for selection
        print(f"Week: {percent_a['W_End']} : Percent: {percent_a['Percentage_1']}")
    if user_choice == 'B'.lower():
        # user gets results for choice B
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_2 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_2']}")

    if user_choice == 'C'.lower():
        # user gets results for choice C
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_3 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_3']}")
    if user_choice == 'D'.lower():
        # user gets results for choice D
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_4 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_4']}")
    if user_choice == 'E'.lower():
        # user gets results for choice E
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_5 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_5']}")
    if user_choice == 'F'.lower():
        # user gets results for choice F
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_6 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_6']}")
    if user_choice == 'G'.lower():
        # user gets results for choice G
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_7 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_7']}")
    if user_choice == 'H'.lower():
        # user gets results for choice H
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_8 > 80]
        # Collects over 80 percent values for selection
        print(f"Week: {percent_a['W_End']} : Percent: {percent_a['Percentage_8']}")


def read_panda_file_question_2():
    """
    Helps answer the question regarding the longest streak of residents not testing
    positive for covid.
    :return:
    returns the value of the longest streaks.
    """

    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    # Reads the csv file
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
    # The above makes the column names manageable.



    provider_list = []
    # Creates an empty list for providers for later use
    provider = ''
    # creates an empty variable for a provider for later use
    count_list = []
    # creates an empty list for counts for later use
    count = 0
    # Creates count variable for later use
    max_count = 0
    # Creates max_count variable for later use
    for row, counter in zip(covid_simple_titles['P_name'], covid_simple_titles['covid_weekly_count']):
        # Used to iterate 2 new variables through 2 columns 'P_name' and 'covid_weekly_count'
        if provider == row:
            if counter < 1:
                count += 1
            else:
                count_list.append(count)
                count = 0

        else:
            if provider_list != [] and max_count != max(count_list): ###
                print(f"Provider: {provider}, Weeks without Covid: {max(count_list)} ")
                max_count = max(count_list)
            provider = row
            provider_list.append(provider)
            count_list = [0]

def read_panda_file_question_3():
    bonus_df = pd.read_csv('bonus_challenge.csv')
    #print(bonus_df)
    no_nan = bonus_df.dropna
    nans = bonus_df-[bonus_df.dropna]
    nan_date_list = []
    for line, date in zip(bonus_df, bonus_df['date_last_administered']):
        try:
            if date == '1':
                print(f"{line}This row lacks a date")
                nan_date_list.append(line)
        except:
            if date < 1:
                print(f"{line}This row lacks a date")
                nan_date_list.append(line)
    print(nan_date_list)
    print(nans)

if __name__ == "__main__":
    main()
