from requests import get
import tabula
import csv
import json


def extract_table_from_pdf():
    while True:
        try:
            # Get & save pdf
            f = open("table.pdf", 'wb')
            f.write(get("https://digitalaccessibility.uoregon.edu/files/2020-11/Table%20Example%20-%20Fixed.pdf", ).content)
            f.close()

            # Read & print data
            csv_data = tabula.read_pdf("table.pdf", format='csv', pages='all', lattice=True, silent=True)
            print(len(csv_data))
            # print(csv_data)

            # Convert & save data in csv
            tabula.convert_into("table.pdf", "data.csv", output_format="csv", pages='all')

            # Convert csv to json
            data = {}
            with open("data.csv") as csv_file:
                # csv_reader = csv.DictReader(csv_file)
                # for rows in csv_reader:
                #     # xd = rows['0']
                #     print(rows['Susan'])
                # reader = csv.reader(csv_file)
                # for rows in reader:
                #     print(reader.line_num)

                # Extract first table data
                data = {}
                i = 0
                for row in csv.DictReader(csv_file):
                    for key, value in row.items():
                        if i == 24:
                            break
                        if key not in data:
                            data[key] = []
                        data[key].append(value)
                        i += 1
                print(data)
            break
        except Exception as e:
            print(e)
            raise


extract_table_from_pdf()

# Note: Maybe there have more efficient way to read csv file
# Please contribute it or suggest me.
