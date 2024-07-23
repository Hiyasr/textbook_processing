from sklearn.mixture import GaussianMixture
from sentence_transformers import SentenceTransformer
import openai
import torch

openai.api_key = 'YOUR_OPENAI_API_KEY'

def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def raptor_indexing(embeddings, texts, max_clusters=5):
    if len(texts) <= 1:
        return [{"text": texts[0], "embedding": embeddings[0].tolist()}]

    # Cluster the embeddings
    gmm = GaussianMixture(n_components=min(max_clusters, len(texts)), covariance_type='full')
    clusters = gmm.fit_predict(embeddings.cpu().numpy())

    cluster_texts = [[] for _ in range(gmm.n_components)]
    for idx, label in enumerate(clusters):
        cluster_texts[label].append(texts[idx])

    summarized_texts = []
    summarized_embeddings = []

    for cluster in cluster_texts:
        if len(cluster) > 0:
            combined_text = " ".join(cluster)
            summary = summarize_text(combined_text)
            summarized_texts.append(summary)
            summarized_embedding = model.encode(summary, convert_to_tensor=True)
            summarized_embeddings.append(summarized_embedding)

    return [{"text": text, "embedding": emb.tolist()} for text, emb in zip(summarized_texts, summarized_embeddings)]

# Example usage with one of the textbooks
raptor_index_textbook1 = raptor_indexing(textbook1_embeddings, textbook1_chunks)
raptor_index_textbook2 = raptor_indexing(textbook2_embeddings, textbook2_chunks)
raptor_index_textbook3 = raptor_indexing(textbook3_embeddings, textbook3_chunks)

print("RAPTOR Indexing for Textbook 1 completed")
print("RAPTOR Indexing for Textbook 2 completed")
print("RAPTOR Indexing for Textbook 3 completed")
