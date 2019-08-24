NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names = [name.title() for name in names]
    names = list(set(names))
    return names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # ...
    # names = [name.title() for name in names ]
    names.sort(key=lambda x: x.split()[-1], reverse=True)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...
    #names = [name.lower() for name in names]
    names.sort(key=lambda x: x.split())
    short_name = min((short for short in names if short), key=len)
    return short_name.split()[0]


print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))
