from requests import get, post, Session
import tabula


def extract_table_from_pdf():
    while True:
        try:
            f = open("table.pdf", 'wb')
            f.write(get("https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf", ).content)
            f.close()
            csv_data = tabula.read_pdf("table.pdf", format='csv', pages='all', lattice=True, silent=True)

            print(len(csv_data))

            print(csv_data)

            break
        except Exception as e:
            print(e)
            raise


extract_table_from_pdf()
