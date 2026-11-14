from models import (
    find_organisations_for,
    find_people,
    add_log,

)

def search(q):
    add_log(f"search: {q}")

    people = find_people(q)

    results = []

    for person in people:

        organsisations = find_organisations_for(person["id"])
                                            
                                            
        results.append({
            "person": person,
            "organisations": organsisations
        })

    return results