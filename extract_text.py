import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

textbook1_pdf_path = r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook1.pdf"
textbook2_pdf_path = r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook2.pdf"
textbook3_pdf_path = r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook3.pdf"

textbook1_text = extract_text_from_pdf(textbook1_pdf_path)
textbook2_text = extract_text_from_pdf(textbook2_pdf_path)
textbook3_text = extract_text_from_pdf(textbook3_pdf_path)

with open(r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook1.txt", "w", encoding="utf-8") as file:
    file.write(textbook1_text)

with open(r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook2.txt", "w", encoding="utf-8") as file:
    file.write(textbook2_text)

with open(r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook3.txt", "w", encoding="utf-8") as file:
    file.write(textbook3_text)

print(f"Extracted {len(textbook1_text)} characters from textbook1.pdf")
print(f"Extracted {len(textbook2_text)} characters from textbook2.pdf")
print(f"Extracted {len(textbook3_text)} characters from textbook3.pdf")
