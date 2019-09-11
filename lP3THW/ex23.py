import sys
script, encoding, error = sys.argv


def main(languages_file, encoding, errors):
    line = languages_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(languages_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string, ", language->", next_lang)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)