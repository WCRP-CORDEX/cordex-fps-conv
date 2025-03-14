import os
import requests
from collections import defaultdict

# Constants for Zotero API
GROUP_ID = "5816477"
COLLECTION_KEY = "SQP8S37V"
API_BASE_URL = f"https://api.zotero.org/groups/{GROUP_ID}/collections/{COLLECTION_KEY}/items"
HEADERS = {"Accept": "application/json"}

OUTPUT_FILE = "docs/publications.md"

def fetch_all_items():
    items = []
    start = 0
    limit = 100

    while True:
        response = requests.get(
            API_BASE_URL,
            headers=HEADERS,
            params={"format": "json", "limit": limit, "start": start}
        )
        if response.status_code != 200:
            raise Exception(f"Failed to fetch Zotero items: {response.status_code}")

        page_items = response.json()
        if not page_items:
            break

        items.extend(page_items)
        start += len(page_items)

    return items

def format_authors(creators):
    authors = [f"{c['lastName']}, {c['firstName'][0]}." for c in creators if c.get("creatorType") == "author" and c.get("lastName")]
    return ", ".join(authors)

def extract_metadata(item):
    data = item.get("data", {})
    creators = data.get("creators", [])
    authors = format_authors(creators)
    title = data.get("title", "Untitled")
    publication = data.get("publicationTitle", data.get("journalAbbreviation", ""))
    year = data.get("date", "")[:4] if data.get("date") else "Unknown"
    doi = data.get("DOI", None)
    url = f"[https://doi.org/{doi}](https://doi.org/{doi})" if doi else data.get("url", "")
    return year, f"{authors}: {title}, {publication}, {url}, {year}."

def generate_markdown(grouped_by_year):
    lines = ["# Publications\n"]
    for year in sorted(grouped_by_year.keys(), reverse=True):
        lines.append(f"## {year}\n")
        for entry in sorted(grouped_by_year[year]):
            lines.append(f" * {entry}")
        lines.append("")  # blank line
    return "\n".join(lines)

def main():
    items = fetch_all_items()
    publications_by_year = defaultdict(list)

    for item in items:
        try:
            year, entry = extract_metadata(item)
            publications_by_year[year].append(entry)
        except Exception as e:
            print(f"Skipping item due to error: {e}")

    markdown = generate_markdown(publications_by_year)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Generated {OUTPUT_FILE} with {sum(len(v) for v in publications_by_year.values())} publications.")

main()

