import re


def find_dates_in_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    dates = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
    return bool(dates)
