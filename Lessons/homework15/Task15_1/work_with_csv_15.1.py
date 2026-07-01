import csv

file_1 = "r-m-c.csv"
file_2 = "random-michaels.csv"


def csv_to_dict(file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))

    column_name_list = reader[0]
    row_values_list = reader[1:]

    all_data_dict = [
        dict(zip(column_name_list, row))
        for row in row_values_list
    ]

    return all_data_dict


data_1 = csv_to_dict(file_1)
data_2 = csv_to_dict(file_2)

all_data = data_1 + data_2

print(f"Rows before removing duplicates: {len(all_data)}")

unique_data = {}

for row in all_data:
    unique_data[row["ContactID"]] = row

result_data = list(unique_data.values())

print(f"Rows after removing duplicates: {len(result_data)}")

with open(
        "result_Turchyna.csv",
        "w",
        newline="",
        encoding="utf-8"
) as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=result_data[0].keys()
    )

    writer.writeheader()
    writer.writerows(result_data)

result_data = []

for row in all_data:
    if row not in result_data:
        result_data.append(row)