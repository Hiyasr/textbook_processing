from sentence_transformers import SentenceTransformer
import nltk
from nltk.tokenize import sent_tokenize

# Download the punkt tokenizer for sentence tokenization
nltk.download('punkt')

def chunk_text(text, max_tokens=100):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    current_tokens = 0

    for sentence in sentences:
        sentence_tokens = len(sentence.split())
        if current_tokens + sentence_tokens <= max_tokens:
            current_chunk += " " + sentence
            current_tokens += sentence_tokens
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
            current_tokens = sentence_tokens

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# Load the SBERT model
print("Loading the SBERT model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("SBERT model loaded.")

# Read the text files and chunk the text
def read_text_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

# Update the file paths as per your system
print("Reading text files...")
textbook1_text = read_text_file(r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook1.txt")
textbook2_text = read_text_file(r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook2.txt")
textbook3_text = read_text_file(r"C:\Users\hiyas\OneDrive\Desktop\CODING\textbook3.txt")
print("Text files read.")

# Chunk the text
print("Chunking text for Textbook 1...")
textbook1_chunks = chunk_text(textbook1_text)
print(f"Textbook 1: {len(textbook1_chunks)} chunks")

print("Chunking text for Textbook 2...")
textbook2_chunks = chunk_text(textbook2_text)
print(f"Textbook 2: {len(textbook2_chunks)} chunks")

print("Chunking text for Textbook 3...")
textbook3_chunks = chunk_text(textbook3_text)
print(f"Textbook 3: {len(textbook3_chunks)} chunks")

# Embed the chunks
print("Embedding chunks for Textbook 1...")
textbook1_embeddings = model.encode(textbook1_chunks, convert_to_tensor=True)
print("Textbook 1 embeddings completed.")

print("Embedding chunks for Textbook 2...")
textbook2_embeddings = model.encode(textbook2_chunks, convert_to_tensor=True)
print("Textbook 2 embeddings completed.")

print("Embedding chunks for Textbook 3...")
textbook3_embeddings = model.encode(textbook3_chunks, convert_to_tensor=True)
print("Textbook 3 embeddings completed.")

print("All embeddings completed.")
