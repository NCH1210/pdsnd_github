import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
df = pd.read_csv(CITY_DATA[city])
    while True:
city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n")
    if city not in ('New York City', 'Chicago', 'Washington'):

    print("Sorry, Try again.")
    continue
    else:
    break

    # TO DO: get user input for month (all, january, february, ... , june)
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
df = df[df['month'] == month]

while True:

month = input("Which month? January, February, March, April or June?\n").lower()

    if month not in months:

    print("Sorry, {} is not a valid month. Please type again".format(month))

else:

    break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)


    # TO DO: display the most common day of week
popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day:', popular_day)


    # TO DO: display the most common start hour
popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
popular_start_station = df['hour'].mode()[0]

    print('Most Popular Start Station', popular_start_station)


    # TO DO: display most commonly used end station
popular_end_station = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    # TO DO: display most frequent combination of start station and end station trip
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
def trip_duration_stats(df):

"""Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

start_time = time.time()

trip_dur = df['Trip Duration'].sum()

    print('Total trip duration: ',trip_dur)


    # TO DO: display mean travel time

mean_travel = df['Trip Duration'].mean()

    print('Mean Travel Time: ',mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
user_types = df['User Type'].value_counts()

    print(user_types)


    # TO DO: Display counts of gender
user_types = df['User Type'].value_counts()

    print('Count of User types: ',user_types)

    if 'Gender' in df:

gender_count = df['Gender'].value_counts()

    print('Total Gender count: ',gender_count)

    else:

    print('Gender information is not available for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
if 'Birth Year' in df:

earliest_birth_year = df['Birth Year'].min()

    print('Earliest Birth Year: ',earliest_birth_year)

    else:

    print('Birth Year information is not available for this city')

    if 'Birth Year' in df:

recent_birth_year = df['Birth Year'].max()

    print('Most recent Birth Year: ',recent_birth_year)

    else:

    print('Birth Year information is not available for this city')

    if 'Birth Year' in df:

common_birth_year = df['Birth Year'].mode()[0]

    print('Most common Birth Year: ',common_birth_year)

    else:

    print('Birth Year information is not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


    if __name__ == "__main__":
	main()
