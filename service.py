from models import find_people, add_log


def search(q):
    add_log(f"search: {q}")

    return find_people(q)
