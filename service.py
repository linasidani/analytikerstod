from models import (
    find_organisations_for,
    find_people,
    find_organisations,
    find_people_for_organisation,
    add_log,

)

def search(q):
    add_log(f"search: {q}")

    results = []

    people = find_people(q)


    for person in people:

        organisations = find_organisations_for(person["id"])
                                            
                                            
        results.append({
            "type": "person",
            "person": person,
            "organisations": organisations,
        })

    organisations = find_organisations(q)

    for organisation in organisations:
        people = find_people_for_organisation(organisation["id"])

        results.append({
                "type": "organisation",
                "organisation": organisation,
                "people": people,
            })

    return results