from pathlib import Path


def load_documents(folder="data/raw"):
    """Read every .txt file in the folder. Returns {document name: text}."""
    docs = {}
    for path in sorted(Path(folder).glob("*.txt")):
        docs[path.stem] = path.read_text(encoding="utf-8")
    return docs


def simple_chunk(text, doc_name, chunk_size=500, overlap=50):
    """Method 1: cut text into fixed-size pieces that overlap slightly."""
    chunks = []
    step = chunk_size - overlap
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append({
            "doc": doc_name,
            "start": start,
            "end": end,
            "text": text[start:end],
        })
        if end == len(text):
            break
        start += step
    return chunks


if __name__ == "__main__":
    docs = load_documents()
    for name, text in docs.items():
        chunks = simple_chunk(text, name)
        print(f"{name}: {len(text)} characters -> {len(chunks)} chunks")
    print("\nFirst chunk of the first document:")
    first_doc = next(iter(docs))
    print(simple_chunk(docs[first_doc], first_doc)[0])