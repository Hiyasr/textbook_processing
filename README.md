# TEXTBOOK PROCESSING AND EMBEDDING WITH SERBT AND RAPTOR

This project processes textbooks by extracting text from PDFs, chunking the text, embedding the chunks using SBERT, and then applying RAPTOR indexing for effective retrieval and summarization.

# Table of Contents
~ Introduction
~ Requirements
~Installation
~Usage

# Steps
      Extracting Text from PDFs
      Chunking Text
      Embedding Chunks
      RAPTOR Indexing
      Contributing


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

python scripts/extract_text.py
python scripts/chunk_and_embed.py
python scripts/raptor_indexing.py

# 


