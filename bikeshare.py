import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for the city
    while True:
        city = input("Enter the name of the city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please enter a valid city.")
    
    # Get user input for month
    while True:
        month = input("Enter the name of the month (e.g., January, February, ..., June) or 'all' for all months: ").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month in months:
            break
        else:
            print("Invalid month name. Please enter a valid month or 'all'.")
    
    # Get user input for day
    while True:
        day = input("Enter the name of the day of the week (e.g., Monday, Tuesday, ..., Sunday) or 'all' for all days: ").lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day in days:
            break
        else:
            print("Invalid day of the week. Please enter a valid day or 'all'.")
    
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
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    if month != 'all':
        month_index = months.index(month) + 1  # Convert month name to month number
        df = df[df['month'] == month_index]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].value_counts().idxmax()
    print(f"The most common month is: {most_common_month}")
    
    most_common_day = df['Day of Week'].value_counts().idxmax()
    print(f"The most common day of the week is: {most_common_day}")
    
    most_common_hour = df['Hour'].value_counts().idxmax()
    print(f"The most common start hour is: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].value_counts().idxmax()
    most_common_end_station = df['End Station'].value_counts().idxmax()
    
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Travel Time'].sum()
    mean_travel_time = df['Travel Time'].mean()
    
    print(f"Total travel time: {total_travel_time} minutes")
    print(f"Mean travel time: {mean_travel_time} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_counts = df['User Type'].value_counts()
    
    # Ensure 'Gender' and 'Birth Year' columns exist in the DataFrame before analyzing them
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
    else:
        gender_counts = "Gender data not available for this dataset."
    
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode().values
def display_data(df):
    """
    Displays 5 lines of raw data upon user request.
    Continues to prompt the user to view additional data in increments of 5 lines.
    Stops when the user says 'no' or there is no more raw data to display.
    """
    start_loc = 0
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ").lower()
    
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()
        
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
