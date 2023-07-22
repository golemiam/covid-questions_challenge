import csv
import pandas as pd
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait

#from pandas_datareader import data
#from pandas.tseries import offsets


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
    #url_read_question_1()
    #open_browser()
    #opener()
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


def opener():
    # the target we want to open
    url = "https://data.cms.gov"

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")

        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')

        # l is the list which contains all the text i.e news
        l = soup.find("a", {"class": "HomepageMostViewedDatasets__button btn btn-primary"})
        print(l)
        # now we want to print only the text part of the anchor.
        # find all the elements of a, i.e anchor
        for i in l.findAll("a"):
            print(i.text)
    else:
        print("Error")
def open_browser():
    driver = webdriver.Chrome(r"C:/Users/Golem/Downloads/chromedriver_win32/chromedriver")
    url = "https://data.cms.gov/covid-19/covid-19-nursing-home-data/data?query=%7B%22filters%22%3A%7B%22rootConjunction%22%3A%7B%22label%22%3A%22And%22%2C%22value%22%3A%22AND%22%7D%2C%22list%22%3A%5B%5D%7D%2C%22keywords%22%3A%22%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22sort%22%3A%7B%22sortBy%22%3Anull%2C%22sortOrder%22%3Anull%7D%2C%22columns%22%3A%5B%22week_ending%22%2C%22federal_provider_number%22%2C%22provider_name%22%2C%22provider_city%22%2C%22provider_state%22%2C%22provider_zip_code%22%2C%22provider_phone_number%22%2C%22residents_weekly_confirmed_covid_19%22%2C%22number_of_all_healthcare_personnel_eligible_to_work_in_this_facility_for_at_least_1_day_this_week_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22recent_percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_with_a_completed_vaccination_who_received_a_covid_19_vaccine_booster_at_any_time%22%2C%22Recent_Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%2C%22Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%5D%7D"

    driver.get(url)
    driver.find_element_by_link_text('export_btn_text').click()
    text_field = driver.find_element_by_link_text('export_btn_text')
    text = wait(driver, 10).until(lambda driver: not text_field.text == 'Export' and text_field.text)
    return text

    print(open_browser())

def url_read_question_1():
    url = "https://data.cms.gov/covid-19/covid-19-nursing-home-data/data?query=%7B%22filters%22%3A%7B%22rootConjunction%22%3A%7B%22label%22%3A%22And%22%2C%22value%22%3A%22AND%22%7D%2C%22list%22%3A%5B%5D%7D%2C%22keywords%22%3A%22%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22sort%22%3A%7B%22sortBy%22%3Anull%2C%22sortOrder%22%3Anull%7D%2C%22columns%22%3A%5B%22week_ending%22%2C%22federal_provider_number%22%2C%22provider_name%22%2C%22provider_city%22%2C%22provider_state%22%2C%22provider_zip_code%22%2C%22provider_phone_number%22%2C%22residents_weekly_confirmed_covid_19%22%2C%22number_of_all_healthcare_personnel_eligible_to_work_in_this_facility_for_at_least_1_day_this_week_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22recent_percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_with_a_completed_vaccination_who_received_a_covid_19_vaccine_booster_at_any_time%22%2C%22Recent_Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%2C%22Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%5D%7D"
    site = requests.get(url)
    response = requests.get(f"{url}/Export")
    print(site.json)
    print(site.elapsed)
    print(site.iter_content)
    print(site.headers)
    print(site.content)
    for i in range(len(site.__dir__())):
        print(site.__dir__()[i])
    print(site.url)

    #print(response.text)


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

    try:
        int(facility_choice[0])
        print("Yes it is")
        facility_choice_other = 0
    except:
        print("No it isn't")
        facility_choice_other = facility_choice.upper()
        facility_choice = 3
    try:
        a = [f"{(facility_choice)}", provider_df]
        print(a)
    except:
        print("test")
    if facility_choice == '1'.lower():
        pass
    elif facility_choice == '2'.lower():
        merger_df = provider_df.merge(right=covid_df, how="left", left_on="our affilitied federal provider numbers", right_on="Federal Provider Number")
        covid_df = merger_df


    elif facility_choice_other != 0:
        print(covid_df[covid_df["Provider Name"].str.lower() == facility_choice_other.lower()])
        providers = covid_df.groupby("Provider Name")
        facility = providers.get_group(facility_choice_other)
        covid_df = facility


    elif f"{str(facility_choice)}" in a:
        providers = covid_df.groupby("Federal Provider Number")
        facility = providers.get_group(facility_choice)
        facility_mix = pd.DataFrame({f'{facility["Provider Name"].values}': range(len(facility))})

        facility.index = facility_mix.index

        covid_df = facility

    try:
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
    except:
        print("No simple titles")
    print("Test for simple")



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
    data = percent_a
    save_to_file(data)


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

    max_count_list = []

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
            max_count_list.append(max_count)
            count_list = [0]

    data = [f"{provider_list}, {max_count_list}"]
    save_to_file(data)

def read_panda_file_question_3():
    bonus_df = pd.read_csv('bonus_challenge.csv', parse_dates= ["date_last_administered"])
    #print(bonus_df)
    no_nan = bonus_df.dropna

    filled_nan = bonus_df.fillna(-1)
    #print(filled_nan.index)
    for i in range(len(filled_nan.iloc[0])):
        #print(i)
        pass
    sorted_employees = filled_nan.sort_values(["employee_id"])
    #print(sorted_employees)
    no_dates = filled_nan["date_last_administered"] == -1
    medically_exempt = filled_nan["medically_exempt"] == 1
    refused = filled_nan["refused"] == 1
    xor_group_1 = filled_nan[no_dates^medically_exempt^refused]
    pfizer_one = filled_nan["got_pfizer1"] == 1
    pfizer_two = filled_nan["got_pfizer2"] == 1
    pfizer_three = filled_nan["got_pfizer3"] == 1
    pfizer_or_group = filled_nan[pfizer_one|pfizer_two|pfizer_three]
    moderna_one = filled_nan["got_moderna1"] == 1
    moderna_two = filled_nan["got_moderna2"] == 1
    moderna_three = filled_nan["got_moderna3"] == 1
    moderna_or_group = filled_nan[moderna_one | moderna_two | moderna_three]
    janssen_one = filled_nan["got_janssen1"] == 1
    janssen_two = filled_nan["got_janssen2"] == 1
    janssen_or_group = filled_nan[janssen_one | janssen_two]
    unknown_one = filled_nan["got_unknown1"] == 1
    unknown_two = filled_nan["got_unknown2"] == 1
    unknown_three = filled_nan["got_unknown3"] == 1
    unknown_or_group = filled_nan[unknown_one | unknown_two | unknown_three]

    print(moderna_or_group)
    #xor_group_2 = filled_nan[moderna_or_group ^ pfizer_or_group ^ janssen_or_group ^ unknown_or_group]
    #This breaks it 
    #print(xor_group_2)

    #print(filled_nan[no_dates])
    print(xor_group_1)

    filled_nan["has_nans"] = "No"
    #print(filled_nan.head(5))
    def rows_with_nans(nan_spots):
        if nan_spots in ["Filled"]:
            return "yes"
    nan_series = filled_nan["has_nans"].apply(rows_with_nans)
    print(nan_series)


    #print(no_nan)
    #nans = [bonus_df-no_nan]
    #print(nans)
    nan_date_list = []
    """
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
    #print(nans)
    """

def save_to_file(data):
    out_file_choice = input("What would you like to name the file? ")
    try:
        with open(out_file_choice, "x") as out_file:
            print(data, file= out_file)
    except:
        out_file_placer = "placer.txt"
        with open(out_file_placer, "w") as out_file:
            print(data, file= out_file)
            print("""
                You chose a file name that has already been taken, 
            your data has been placed in placer.txt and will be 
            overwritten when this program runs again. Either choose 
            a new file name where you would like this saved, or view 
            the data now before it gets removed. 
            """)


if __name__ == "__main__":
    main()
