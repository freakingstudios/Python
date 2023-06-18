import PyPDF2
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def convert_pdf_to_xml(pdf_path, xml_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    root = ET.Element('root')
    question_num = 1
    question = None

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text().strip()

        # Split text into lines
        lines = text.split('\n')

        for line in lines:
            line = line.strip()
            if line.endswith('?'):  # Assuming lines ending with '?' are questions
                question = ET.SubElement(root, 'question', {'id': f'Q{question_num}'})
                question.text = line
                question_num += 1
            elif line and question is not None:  # Assuming non-empty lines without '?' are answers
                answer = ET.SubElement(question, 'answer')
                answer.text = line

    xml_string = ET.tostring(root, encoding='utf-8')
    xml_pretty_string = minidom.parseString(xml_string).toprettyxml(indent="    ")

    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_pretty_string)

    print("PDF converted to XML successfully!")

# Example usage
pdf_file = 'javaq.pdf'
xml_file = 'example.xml'
convert_pdf_to_xml(pdf_file, xml_file)
