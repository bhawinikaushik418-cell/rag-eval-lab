from src.chunking import simple_chunk


def test_chunks_cover_whole_text():
    text = "a" * 1234
    chunks = simple_chunk(text, "demo", chunk_size=500, overlap=50)
    assert chunks[0]["start"] == 0
    assert chunks[-1]["end"] == len(text)


def test_chunks_overlap():
    text = "a" * 1234
    chunks = simple_chunk(text, "demo", chunk_size=500, overlap=50)
    assert chunks[1]["start"] == chunks[0]["end"] - 50


def test_chunk_text_matches_span():
    text = "abcdefghij" * 100
    for c in simple_chunk(text, "demo"):
        assert c["text"] == text[c["start"]:c["end"]]