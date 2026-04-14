import xml.etree.ElementTree as ET
import sys
import re

def extract_text(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # namespaces in docx
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    # iterate over all paragraphs
    for p in root.findall('.//w:p', ns):
        texts = []
        for t in p.findall('.//w:t', ns):
            if t.text:
                texts.append(t.text)
        if texts:
            print("".join(texts))

if __name__ == "__main__":
    extract_text(sys.argv[1])
