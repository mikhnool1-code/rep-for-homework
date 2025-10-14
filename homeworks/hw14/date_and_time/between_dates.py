from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_days_between(date1, date2):
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.strptime(date2, "%Y-%m-%d").date()
        return abs((d2 - d1).days)
    except ValueError:
        return "Wrong datetime format or incorrect date"
