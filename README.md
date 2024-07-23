Textbook Processing and Embedding with SBERT and RAPTOR Indexing
This project processes textbooks by extracting text from PDFs, chunking the text, embedding the chunks using SBERT, and then applying RAPTOR indexing for effective retrieval and summarization.

Table of Contents
Introduction
Requirements
Installation
Usage
Project Structure
Steps
      Extracting Text from PDFs
      Chunking Text
      Embedding Chunks
      RAPTOR Indexing
      Contributing


Introduction
This project aims to extract, process, and embed text from digital textbooks. The goal is to create a question-answering system using Large Language Models (LLMs) and efficient retrieval techniques like RAPTOR indexing.

Requirements
Python 3.7 or higher
Virtualenv (optional but recommended)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/textbook-processing.git
cd textbook-processing
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Place your PDF textbooks in the pdfs directory.
Run the text extraction script:
bash
Copy code
python scripts/extract_text.py
Run the chunking and embedding script:
bash
Copy code
python scripts/chunk_and_embed.py
Run the RAPTOR indexing script:
bash
Copy code
python scripts/raptor_indexing.py
Project Structure
arduino
Copy code
textbook-processing/
│
├── pdfs/
│   ├── textbook1.pdf
│   ├── textbook2.pdf
│   └── textbook3.pdf
│
├── text/
│   ├── textbook1.txt
│   ├── textbook2.txt
│   └── textbook3.txt
│
├── embeddings/
│   ├── textbook1_embeddings.pt
│   ├── textbook2_embeddings.pt
│   └── textbook3_embeddings.pt
│
├── scripts/
│   ├── extract_text.py
│   ├── chunk_and_embed.py
│   └── raptor_indexing.py
│
├── requirements.txt
└── README.md


Steps
Extract Text from PDFs

Use the extract_text.py script to extract text from PDF textbooks and save them as text files.



python extract_text.py
Chunk Text and Create Embeddings

Use the chunks_text.py script to chunk the text into manageable pieces and create embeddings using the SBERT model.



python chunks_text.py
RAPTOR Indexing and Summarization

Use the raptor_indexing.py script to perform RAPTOR indexing on the text chunks and summarize the text.



python raptor_indexing.py
File Descriptions
extract_text.py: Extracts text from PDF textbooks.
chunks_text.py: Chunks the extracted text and creates embeddings using SBERT.
raptor_indexing.py: Performs RAPTOR indexing on the text chunks and summarizes the text.

Example Usage
Ensure to update the file paths and OpenAI API key as per your system configuration before running the scripts.
