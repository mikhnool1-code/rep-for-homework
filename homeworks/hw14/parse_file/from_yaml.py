import yaml


def read_books(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            return data["books"]
    except TypeError:
        return "Wrong YAML format or file error"


def add_book(title, author, year, filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        new_book = {"author": author, "title": title, "year": year}
        data["books"].append(new_book)

        save_books(data, filename)
        return data["books"]
    except TypeError:
        return "Wrong YAML format or file error"


def save_books(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file)
    except TypeError:
        return "Wrong YAML format or file error"
