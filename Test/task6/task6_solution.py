def analyze_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        text = "".join(lines)

    file_length = len(lines)
    words_count = len(text.split())
    letters_count = sum(ch.isalpha() for ch in text)

    result = f"Строк: {file_length}, Слов: {words_count}, Букв: {letters_count}"

    print(result)

    with open(filename, "a", encoding="utf-8") as file:
        file.write(result)

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    assert "Строк:" in content and "Слов:" in content and "Букв:" in content, \
        "Данные не были добавлены в файл!"

