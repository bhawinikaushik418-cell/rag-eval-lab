import requests
import yaml
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def fetch_wikipedia(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query", "prop": "extracts", "explaintext": 1,
        "titles": title, "format": "json",
    }
    headers = {"User-Agent": "rag-eval-lab/0.1 (learning project)"}
    data = requests.get(url, params=params, headers=headers).json()
    page = next(iter(data["query"]["pages"].values()))
    return page["extract"]

with open("data/sources.yaml") as f:
    sources = yaml.safe_load(f)["sources"]

for s in sources:
    if s["type"] == "wikipedia":
        text = fetch_wikipedia(s["title"])
        (RAW_DIR / f"{s['name']}.txt").write_text(text, encoding="utf-8")
        print(f"Saved {s['name']} ({len(text)} characters)")