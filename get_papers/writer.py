import csv

def save_to_file(data, filename):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def print_to_screen(data):
    for row in data:
        for key, value in row.items():
            print(f"{key}: {value}")
        print("-" * 40)
