import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
DAYS_DICT = {
    1: 'Sunday', 2: 'Monday',
    3: 'Tuesday', 4: 'Wednesday',
    5: 'Thursday', 6: 'Friday', 7: 'Saturday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    Cities = ['chicago', 'new york', 'washington']
    Months = ['january', 'february', 'march', 'april', 'may', 'june','all']

    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        print('Would you like to see data for Chicago, New york, or washington ?')
        city = str(input().lower())
        if city not in Cities:
            print('Please,Enter Valid City')
            continue
        else:
            break

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('Which month? January, February, March, April, May, or June?')
        # get user input for month (all, january, february, ... , june)
        month = str(input().lower())
        if month not in Months:
            print('Please,Enter Valid Month')
            continue
        else:
            month = month.title()
            break

        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('Which day? Please type your response as an integer (e.g., 1=Sunday).')
        day_index =input()
        if type(day_index) is str:
            day_index = day_index.title()
        if day_index not in DAYS_DICT.keys():
            if day_index == 'All':
                day = day_index
            else:
             print('Please,Enter Valid Day')
             continue
        else:
            day = DAYS_DICT.get(day_index)
        break
    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    last_col = len(df.columns)

    df.insert(last_col, "Month", df['Start Time'].dt.month_name(locale='English'))
    df.insert(last_col + 1, "Day", df['Start Time'].dt.day_name(locale='English'))
    df.insert(last_col + 2, "Hour", pd.to_datetime(df['Start Time']).dt.hour)
    if (month =='All') & (day!='All'):
        df = df.loc[(df['Day'] == day)]
    if (day =='All') & (month!= 'All'):
        df = df.loc[(df['Month'] == month)]
    if (month!='All')&(day!='All'):
        df = df.loc[(df['Day'] == day)&(df['Month']== month)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Popular Month is ', df['Month'].value_counts().idxmax(), ', count', df['Month'].value_counts().max())

    # TO DO: display the most common day of week
    print('Most Popular Day is ', df['Day'].value_counts().idxmax(), ', count', df['Day'].value_counts().max())

    # TO DO: display the most common start hour
    print('Most Popular Hour is ', df['Hour'].value_counts().idxmax(), ', count', df['Hour'].value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station is ', df['Start Station'].value_counts().idxmax(), ', count',
          df['Start Station'].value_counts().max())

    # TO DO: display most commonly used end station
    print('Most commonly used end station is ', df['End Station'].value_counts().idxmax(), ', count',
          df['End Station'].value_counts().max())

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}" \
          .format(most_common_start_end_station[0], most_common_start_end_station[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    count = df['Trip Duration'].sum()
    print('Total Duration:', count, ' ,Count: ', len(df))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('Mean travel time : ',mean)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Customer_len = len(df.loc[df['User Type'] == 'Customer'])
    Dependent_len = len(df.loc[df['User Type'] == 'Dependent'])
    Subscriber_len = len(df.loc[df['User Type'] == 'Subscriber'])
    print('Customer : ', Customer_len,'Subscriber: ',Subscriber_len, ', Dependent: ', Dependent_len)

    # TO DO: Display counts of gender
    female_len = len(df.loc[df['Gender'] == 'Female'])
    male_len = len(df.loc[df['Gender'] == 'Male'])
    print('Male : ', male_len, ', Female: ', female_len)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_Byear=int(df['Birth Year'].min())
    recent_Byear=int(df['Birth Year'].max())
    most_common_Byear=int (df['Birth Year'].value_counts().idxmax())
    print('earliest Year of Birth: ,',earliest_Byear,' most recent Year of Birth: ',recent_Byear,' most commonYear of Birth: ',most_common_Byear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
