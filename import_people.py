import csv
from models import add_person

with open("people.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        add_person(row["name"], row["notes"])

        print("CSV import completed!")