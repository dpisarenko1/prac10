def seconds_since_year_start(datetime_str):
    try:
        parts = datetime_str.split()
        if len(parts) != 2:
            return None

        date = parts[0].split('/')
        time = parts[1].split(':')

        if len(date) != 3 or len(time) != 3:
            return None

        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        hour = int(time[0])
        minute = int(time[1])
        second = int(time[2])

        if not (1 <= month <= 12 and 1 <= day <= 31 and 0 <= hour <= 23 and
            0 <= minute <= 59 and 0 <= second <= 59):
            return None

        days_in_month = [31 ,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29

        if day > days_in_month[month - 1]:
            return None

        days_passed = sum(days_in_month[:month - 1]) + day - 1

        total_sec = (days_passed * 24 * 3600 + hour * 3600 +
                     minute * 60 + second)

        return total_sec

    except:
        return None

print(seconds_since_year_start('11/19/2026 18:12:33'))