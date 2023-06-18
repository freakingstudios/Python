import docx
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def convert_docx_to_xml(docx_path, xml_path):
    doc = docx.Document(docx_path)

    root = ET.Element('root')
    question_num = 1
    question = None

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()

        if text.endswith('?'):  # Assuming paragraphs ending with '?' are questions
            question = ET.SubElement(root, 'question', {'id': f'Q{question_num}'})
            question.text = text
            question_num += 1
        elif text and question is not None:  # Assuming non-empty paragraphs without '?' are answers
            answer = ET.SubElement(question, 'answer')
            answer.text = text

    xml_tree = ET.ElementTree(root)
    xml_string = ET.tostring(root, encoding='utf-8')

    xml_pretty_string = minidom.parseString(xml_string).toprettyxml(indent='  ')
    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_pretty_string)

    print("DOCX converted to XML successfully!")

# Example usage
docx_file = 'javaq.docx'
xml_file = 'example1.xml'
convert_docx_to_xml(docx_file, xml_file)
