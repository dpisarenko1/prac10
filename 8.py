from datetime import datetime


def convert_datetime(date_str):
    """
    convert date string to datetime
    :param date_str: date string
    :return: datetime
    """
    try:
        parts_of_date = date_str.split()
        if len(parts_of_date) != 2:
            return None

        date = parts_of_date[0].split('/')
        time = parts_of_date[1].split(':')

        if len(date) != 3 or len(time) != 3:
            return None

        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        hour = int(time[0])
        minute = int(time[1])
        second = int(time[2])

        if not (1 <= month <= 12):
            return None
        if not (1 <= day <= 31):
            return None
        if not (0 <= hour <= 23):
            return None
        if not (0 <= minute <= 59):
            return None
        if not (0 <= second <= 59):
            return None

        year_new = year % 100

        if hour >= 12:
            period = 'AM'
        if hour == 0:
            hour_12 = 12
        elif hour > 12:
            hour_12 = hour - 12
        else:
            hour_12 = hour

        return f"{day:02}.{month:02}.{year_new:02} {hour_12:02}:{minute:02}:{second:02} {period}"

    except:
        return None


print(convert_datetime('12/12/1998 18:12:38'))

print(convert_datetime('12/12/1998 18:12:38'))
