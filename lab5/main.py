import re

f = "row.txt"

with open(f, "r", encoding = 'UTF-8') as file:
    content = file.read()

    match = re.search(r'ИТОГО(.*)', content, re.DOTALL)

    if match:
        print(match.group(1).strip())
    else:
        print("слово ИТОГО не найдено")