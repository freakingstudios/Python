import os
import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def excel_to_xml(sheet_key, sheet_name, xml_file):
    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet
    sheet = client.open_by_key(sheet_key)
    worksheet = sheet.worksheet(sheet_name)

    # Read data from the Google Sheet
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    # Create the root element of the XML tree
    root = ET.Element('questions')

    # Iterate over each row in the dataframe
    for _, row in df.iterrows():
        # Create a child element for each row
        record = ET.SubElement(root, 'question')

        # Create a sub element for the question and set the value
        question = ET.SubElement(record, 'text')
        question.text = str(row['Question'])

        # Create a sub element for the answer and set the value
        answer = ET.SubElement(record, 'answer')
        answer.text = str(row['Answer'])

    # Create the XML tree from the root element
    tree = ET.ElementTree(root)

    # Convert the XML tree to a pretty-printed string
    xml_string = prettify(root)

    # Build the full output file path
    output_dir = r'C:\Users\jeremiahkalaiselvan\Documents\Projects\JobFinderPlus\Website'
    output_path = os.path.join(output_dir, xml_file)

    # Write the XML string to the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xml_string)

# Usage example
sheet_key = ''
sheet_name = 'SM'
excel_to_xml(sheet_key, sheet_name, 'sm.xml')
