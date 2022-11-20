def percent_to_float(s: str) -> float:
    if s == "":
        return 0.0
    s = s.strip("%")
    s = s.replace(",", ".")
    return round(float(s) / 100, 2)


def string_to_int(s: str) -> int | None:
    res = s.replace("\xa0", "")
    if not res.isdigit():
        return None
    return int(res)


def interval_converter(x: str):
    x = x.split('-')[0]
    x = x.replace(',', '.')
    try:
        return float(x)
    except ValueError:
        return 0
