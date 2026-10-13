
import re

from mcp.server.fastmcp import FastMCP
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

mcp = FastMCP("PDF Document Search")


def split_into_chunks(text, chunk_size=180, overlap=40):
    words = re.findall(r"\S+", text)
    chunks = []
    start = 0

    while start < len(words):
        chunk = " ".join(words[start:start + chunk_size])

        if chunk.strip():
            chunks.append(chunk)

        if start + chunk_size >= len(words):
            break

        start += chunk_size - overlap

    return chunks


@mcp.tool()
def search_pdf(document_text: str, question: str) -> str:
    """Search PDF text and return passages relevant to a question.

    Args:
        document_text: Text extracted from a PDF document.
        question: The question to search for.
    """
    if not document_text.strip() or not question.strip():
        return "Please provide both document text and a question."

    chunks = split_into_chunks(document_text)

    if not chunks:
        return "No searchable text was found."

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )

        chunk_vectors = vectorizer.fit_transform(chunks)
        question_vector = vectorizer.transform([question])

        scores = cosine_similarity(
            question_vector, chunk_vectors
        ).flatten()

    except ValueError:
        return "Could not find searchable terms in the document."

    ranked = scores.argsort()[::-1][:3]

    results = [
        f"Passage {i + 1} (score: {scores[index]:.3f}):\n"
        f"{chunks[index]}"
        for i, index in enumerate(ranked)
        if scores[index] > 0
    ]

    if not results:
        return "No relevant passages found in the document."

    return "\n\n".join(results)


if __name__ == "__main__":
    mcp.run(transport="stdio")
