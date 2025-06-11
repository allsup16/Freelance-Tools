from datetime import timedelta, datetime

year = ['Y','y','year','YEAR','Year','years','YEARS','Years']
month = ['M','m','month','MONTH','Month','months','MONTHS','Months','mo']
day = ['D','d','day','DAY','Day','days','DAYS','Days']
hour = ['H','h','hour','HOUR','Hour','hours','HOURS','Hours']
minutes = ['M','m','minute','MINUTE','Minute','minutes','MINUTES','Minutes','min']
seconds = ['S','s','second','SECOND','Second','seconds','SECONDS','Seconds']

def convert(time,unit_time):
    now = datetime.now()
    try:
        time = int(time)
    except ValueError:
        print('Invalid time  format')
        return None

    if unit_time in year:
        result = now - timedelta(days=365*time)
    elif unit_time in month:
        result = now - timedelta(days=30*time)
    elif unit_time in day:
        result = now - timedelta(days=time)
    elif unit_time in hour:
        result = now - timedelta(hours=time)
    elif unit_time in minutes:
        result = now - timedelta(minutes=time)
    elif unit_time in seconds:
        result = now - timedelta(seconds=time)
    else:
        return None
    return result
    