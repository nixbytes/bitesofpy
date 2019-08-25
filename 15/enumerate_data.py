names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    names_countries = dict(zip(names, countries))

    count = 1

    for key, value in names_countries.items():
        print(f"{count}. {key:<10}      {value}")
        count += 1


enumerate_names_countries()
