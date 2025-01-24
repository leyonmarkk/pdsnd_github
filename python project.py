# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:47:26 2025

@author: Katherine Leyonmark
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

cities = ("Chicago", "New York City", "Washington")
months = ("All", "January", "February", "March", "April", "May", "June")
days = ("All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please select Chicago, New York City or Washington: ").title()
        if city in cities:
            break
        else:
            print("City not valid, please enter a valid city")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please select a month up until and including June, or all: ").title()
        if month in months:
            break
        else:
            print("Month not valid, please enter a valid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please select a day of the week or all: ").title()
        if day in days:
            break
        else:
            print("Day not valid, please enter a valid day")
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def raw_data(df):
        count = 5
        raw_data = input("Would you like to see 5 lines of raw data? yes/no :").title()
        if raw_data == "Yes":
                print(df.head(count))
                while True:
                        next_rows = input("Would you like to see 5 more lines? yes/no :").title()
                        if next_rows == "Yes":
                            count = count + 5
                            print(df.head(count))
                        elif next_rows == "No":
                            break
                        else:
                            print("This is not a valid input, try again")
        elif raw_data != "Yes" or raw_data != "No":
            print("This is not a valid input, try again")
            
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    ## extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    ## extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.dayofweek
    
    popular_day = df['day'].mode()[0]

    print('Most Popular Start Day:', popular_day)

    # TO DO: display the most common start hour
    ## extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    ## find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_station)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_endstation)


    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + " To " + df['End Station']
    popular_combo = df['combo'].mode()[0]

    print('Most Popular Start/End Station Combination:', popular_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print("The total trip duration is: ", total)
 
    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print("The average trip duration is: ", mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("There are ", user_types, " users.")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print("The gender counts are: ", genders)
    else:
        print("Washington does not have gender information.")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()
        print("The earliest birth year is :", early)
        print("The most recent birth year is :", recent)
        print("The most common birth year is :", common)
    else:
        print("Washington does not have birth year information.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
