import re

def tally_words(content):
    counts = {}
    tokens = re.findall(r"[\w']+", content.casefold())
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1
    return counts

def run_app():
    content = input("Enter a sentence or paragraph: ").strip()
    counts = tally_words(content)
    if not counts:
        print("No words were found.")
        return
    print("\n========== WORD FREQUENCIES ==========")
    print(f"{'Word':<25} Count")
    print("-" * 33)
    for token, qty in sorted(counts.items()):
        print(f"{token:<25} {qty}")

if __name__ == "__main__":
    run_app()
