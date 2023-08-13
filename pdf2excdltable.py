import camelot
import pandas as pd


def convert_pdf_to_excel(pdf_path, output_path):
    # Read the PDF and extract tables
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')

    # Save each table as a separate sheet in the Excel file
    with pd.ExcelWriter(output_path) as writer:
        for i, table in enumerate(tables, start=1):
            table.df.to_excel(writer, sheet_name=f"Sheet{i}", index=False)


# Specify the path of the PDF file
pdf_path = 'sample.pdf'

# Specify the output Excel file path
output_path = 'file.xlsx'

# Convert the PDF to Excel
convert_pdf_to_excel(pdf_path, output_path)
