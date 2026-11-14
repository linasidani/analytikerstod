import csv
from models import add_person, find_people

with open("people.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        existing_people = find_people(row["name"])

        if existing_people:
            print(f"Skipped existing person: {row['name']}")
        else:
            add_person(row["name"], row["notes"])
            print(f"Added person: {row['name']}")


print("CSV import completed!")