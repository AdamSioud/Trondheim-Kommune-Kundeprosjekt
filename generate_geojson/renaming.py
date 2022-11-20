def rename_age(x):
    for key in x:
        x[key]["portion"] = x[key].pop("Andel")
        x[key]["quantity"] = x[key].pop("Antall")


def rename_price(x):
    for key in x:
        x[key]["averagePrice"] = x[key].pop("Gjennomsnittspris")
        x[key]["quantity"] = x[key].pop("Antall")


def rename_neighborhood(x):
    for key in x:
        x[key]["portion"] = x[key].pop("Andel")


def rename_interval(x):
    for key in x:
        x[key]["interval"] = x[key].pop("intervall")
