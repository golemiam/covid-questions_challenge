import csv
import pandas as pd

def main():
    """
    Main program for addressing challenge questions
    :return:
    Returns values based on user input
    """


    read_panda_file_question_1()
def read_panda_file_question_1():
    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    covid_simple_titles = covid_df.rename(columns= {'Week Ending': 'W_End', 'Federal Provider Number': 'FP_num', 'Provider Name': 'P_name', 'Provider City': 'P_city', 'Provider State': 'P_state', 'Provider Zip Code': 'P_zip', 'Provider Phone Number': 'P_Phone_#', 'Residents Weekly Confirmed COVID-19': 'Cov_residents', 'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time': 'HCP#_vacc', 'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_1', 'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_2', 'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_3', 'Number of Healthcare Personnel with a Completed Vaccination Eligible to Work in this Facility for At Least 1 Day This Week who Received a COVID-19 Vaccine Booster at Any Time': 'HCP#_2', 'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_4', 'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_5', 'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_6', 'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_7', 'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines': 'Percentage_8'})
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
        print(covid_simple_titles.Percentage_1[(covid_simple_titles.Percentage_1>80)])
    if user_choice == 'B'.lower():
        print(covid_simple_titles.Percentage_2[(covid_simple_titles.Percentage_2 > 80)])
    if user_choice == 'C'.lower():
        print(covid_simple_titles.Percentage_3[(covid_simple_titles.Percentage_3 > 80)])
    if user_choice == 'D'.lower():
        print(covid_simple_titles.Percentage_4[(covid_simple_titles.Percentage_4 > 80)])
    if user_choice == 'E'.lower():
        print(covid_simple_titles.Percentage_5[(covid_simple_titles.Percentage_5 > 80)])
    if user_choice == 'F'.lower():
        print(covid_simple_titles.Percentage_6[(covid_simple_titles.Percentage_6 > 80)])
    if user_choice == 'G'.lower():
        print(covid_simple_titles.Percentage_7[(covid_simple_titles.Percentage_7 > 80)])
    if user_choice == 'H'.lower():
        print(covid_simple_titles.Percentage_8[(covid_simple_titles.Percentage_8 > 80)])
    print(covid_df.info())





if __name__ == "__main__":
    main()
