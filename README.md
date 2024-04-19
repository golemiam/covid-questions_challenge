This file is for processing medical data relating to covid 19. I was given a challenge to answer a series of questions. 

Prompt:
 
Feel free to use any language you’d like.  Python and SQL preferred.
 
Coding Challenge #1:
For each state that Ensign operates in, on which [week_ending] did the average of completed
vaccinations exceed 80% for our healthcare personnel?
 
Coding Challenge #2:
For each of the Ensign providers, what is their longest streak (number of weeks) of residents not testing
positive for Covid-19?  Hint: use the [residents_weekly_confirmed_covid_19] column.
 
The data:
 Our_Provider_numbers.xlsx (attached): a list of our providers
 You can find the Covid-19 Nursing Home Data: https://data.cms.gov/covid-19/covid-19-nursing-
home-data 
o In addition to the data, there are a lot of documentation and material for better
understanding this dataset that we encourage you to familiarize yourself with!

Bonus Challenges
 
Bonus Challenge #1:
Using the attached bonus_challenge.xlsx, there are few records containing bad data.  List out the bad
data.
 
Bonus Challenge #2:
Below is the definition of what it means to have an “up-to-date” vaccination status.  Using the attached
bonus_challenge.xlsx, write a SQL query that calculates whether an individual is up-to-date or not.
 
/*
 
Definition of fully vaccinated:
1. Received both doses of Pfizer or Moderna.
2. Received one dose of Janssen (J&amp;J).
3. Received two doses of Novavax.
 
*/
select employee_id,
       iif(got_pfizer1 = 1 and got_pfizer2 = 1, 0, 1) as fully_vaccinated_pfizer,
       iif(got_moderna1 = 1 and got_moderna1 = 1, 1, 0) as fully_vaccinated_moderna,
       iif(got_unknown1 = 1 and got_unknown2 = 1, 1, 0) as fully_vaccinated_unknown,
       iif(got_novavax1 = 1 or got_novavax2 = 1, 1, 0) as fully_vaccinated_novavax,
       iif(isJanssen1 = 1, 1, 0) as janssen



In order to run this you will need to install python, and an IDE (I have been using pycharm), then you will need to make sure each of the imports listed are installed on your computer, 
then add them to your IDE so that it will process it correctly.
