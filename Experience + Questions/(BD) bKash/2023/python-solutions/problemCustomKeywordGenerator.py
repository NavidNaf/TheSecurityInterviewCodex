import csv
from pathlib import Path


def read_column_from_csv(file_path, column_name):
    values = []

    # Read the requested column from the CSV file.
    with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            values.append(row[column_name])

    return values


def create_keywords(users, passwords):
    keywords = []

    # Pair each username with the password from the same row number.
    for username, password in zip(users, passwords):
        username_part = username[:3]
        password_part = password[-4:]
        keyword = username_part + password_part
        keywords.append(keyword)

    return keywords


def write_keywords(output_file, keywords):
    # Write one generated keyword per line.
    with open(output_file, "w", encoding="utf-8") as file:
        for keyword in keywords:
            file.write(keyword + "\n")


def main():
    current_dir = Path(__file__).resolve().parent
    artifact_dir = current_dir.parent / "python2-artifacts"

    users_file = artifact_dir / "users.csv"
    passwords_file = artifact_dir / "pass.csv"
    output_file = current_dir / "keywords.txt"

    users = read_column_from_csv(users_file, "NAME")
    passwords = read_column_from_csv(passwords_file, "PASSWORD")
    keywords = create_keywords(users, passwords)
    write_keywords(output_file, keywords)

    print("Generated keywords written to:", output_file)


if __name__ == "__main__":
    main()
