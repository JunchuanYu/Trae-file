import docx
import sys

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        for i, para in enumerate(doc.paragraphs):
            if para.text.strip():
                print(f"[{i}] {para.text}")
    except Exception as e:
        print(f"Error reading docx: {e}")

if __name__ == "__main__":
    read_docx(sys.argv[1])
