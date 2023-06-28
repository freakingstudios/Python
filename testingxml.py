import os

import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def prettify(elem):
    # Return a pretty-printed XML string representation of the element
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def excel_to_xml(excel_file, xml_file):
    # Read Excel file using pandas
    df = pd.read_excel(excel_file)

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
excel_to_xml('pythonprogram.xlsx','pythonprogram.xml')
