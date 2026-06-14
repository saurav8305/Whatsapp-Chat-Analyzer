import re
import pandas as pd

def preprocess(data):
    data = data.replace('\u202f', ' ').replace('\xa0', ' ')
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s*(?:am|pm|AM|PM)\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'([^:]+):\s', message, maxsplit=1)
        if len(entry) > 2:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    day_order = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    df['day_name'] = pd.Categorical(
        df['day_name'],
        categories=day_order,
        ordered=True
    )
    period = []
    for hour in df['hour']:
        start = pd.Timestamp(f'{hour}:00').strftime('%I %p').lstrip('0')
        end = pd.Timestamp(f'{(hour + 1) % 24}:00').strftime('%I %p').lstrip('0')
        period.append(f"{start} - {end}")
    df['period'] = period
    period_order = [
        '12 AM - 1 AM',
        '1 AM - 2 AM',
        '2 AM - 3 AM',
        '3 AM - 4 AM',
        '4 AM - 5 AM',
        '5 AM - 6 AM',
        '6 AM - 7 AM',
        '7 AM - 8 AM',
        '8 AM - 9 AM',
        '9 AM - 10 AM',
        '10 AM - 11 AM',
        '11 AM - 12 PM',
        '12 PM - 1 PM',
        '1 PM - 2 PM',
        '2 PM - 3 PM',
        '3 PM - 4 PM',
        '4 PM - 5 PM',
        '5 PM - 6 PM',
        '6 PM - 7 PM',
        '7 PM - 8 PM',
        '8 PM - 9 PM',
        '9 PM - 10 PM',
        '10 PM - 11 PM',
        '11 PM - 12 AM'
    ]
    df['period'] = pd.Categorical(
        df['period'],
        categories=period_order,
        ordered=True
    )
    return df