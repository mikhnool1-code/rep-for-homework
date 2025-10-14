from datetime import datetime, date


def is_future(date1):
    try:
        entered_date = datetime.strptime(date1, "%Y-%m-%d").date()
        today = date.today()

        if entered_date > today:
            return True
        elif entered_date < today:
            return False
        else:
            return None
    except ValueError:
        return "Wrong datetime format or incorrect date"
