def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        fields = [value.strip() for value in line.split(",")]

        if header is None:
            header = fields
            continue

        if len(fields) != len(header):
            continue

        rows.append(dict(zip(header, fields)))

    return rows

def count_types(rows: list[dict]) -> dict:
    counts = {}

    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1

    return counts

def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row["тип"] != kind:
            continue

        try:
            minutes = float(row["минуты"].replace(",","."))
        except ValueError:
            continue

        total += minutes

    return round(total, 1)