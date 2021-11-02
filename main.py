from requests import get
import tabula


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
            print(csv_data[0])

            # Convert & save data in csv
            tabula.convert_into("table.pdf", "data.csv", output_format="csv", pages='all')

            break
        except Exception as e:
            print(e)
            raise


extract_table_from_pdf()
