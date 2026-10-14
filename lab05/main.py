from tablestats import *
from pathlib import Path

def main() -> None:
    path = input().strip()

    with open(path, encoding="utf-8") as table:
        rows = read_rows(table)

    counts = count_types(rows)

    print(len(counts))
    print(len(rows))
    print(f"{total_minutes(rows, 'ошибка'):.1f}")

    summary_path = Path(__file__).with_name("summary.csv")
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

if __name__ == "__main__":
    main()