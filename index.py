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


    covid_count = covid_simple_titles['covid_weekly_count']
    s = pd.Series(covid_count)


    provider_list = []
    provider = ''
    count_list = []
    count = 0
    max_count = 0
    for row, counter in zip( covid_simple_titles['P_name'], covid_simple_titles['covid_weekly_count']):
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

if __name__ == "__main__":
    main()
