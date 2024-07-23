# TEXTBOOK PROCESSING AND EMBEDDING WITH SERBT AND RAPTOR

This project processes textbooks by extracting text from PDFs, chunking the text, embedding the chunks using SBERT, and then applying RAPTOR indexing for effective retrieval and summarization.

# Table of Contents
- Introduction
- Requirements
- Installation
- Usage

# Steps
      - Extracting Text from PDFs
      - Chunking Text
      - Embedding Chunks
      -  RAPTOR Indexing
      


# Introduction
This project aims to extract, process, and embed text from digital textbooks. The goal is to create a question-answering system using Large Language Models (LLMs) and efficient retrieval techniques like RAPTOR indexing.

# Requirements
~ Python 3.7 or higher
~ Virtualenv (optional but recommended)

# Installation

# Clone the repository:
 git clone https://github.com/your-username/textbook-processing.git
cd textbook-processing

# Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Usage
Place your PDF textbooks in the pdfs directory.

# Run the text extraction script, chunking and embeddind script and RAPTOR Script

- python scripts/extract_text.py
- python scripts/chunk_and_embed.py
- python scripts/raptor_indexing.py

# Steps
- Use the extract_text.py script to extract text from PDF textbooks and save them as text files.

python extract_text.py

- Use the chunks_text.py script to chunk the text into manageable pieces and create embeddings using the SBERT model.

  python chunks_text.py

- Use the raptor_indexing.py script to perform RAPTOR indexing on the text chunks and summarize the text.

  python raptor_indexing.py

# Example Usage
Ensure to update the file paths and OpenAI API key as per your system configuration before running the scripts.


# textbook link
 - textbook1: https://people.engr.tamu.edu/guni/csce421/files/AI_Russell_Norvig.pdf
 - textbook2: https://www.ucg.ac.me/skladiste/blog_44233/objava_64433/fajlovi/Computer%20Networking%20_%20A%20Top%20Down%20Approach,%207th,%20converted.pdf
 - textbook3: https://www.uoitc.edu.iq/images/documents/informatics-institute/Competitive_exam/DataStructures.pdf



