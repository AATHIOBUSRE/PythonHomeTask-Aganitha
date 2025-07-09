import argparse
from get_papers.pubmed import fetch_id, fetch_details
from get_papers.parser import parse_article
from get_papers.writer import save_to_file, print_to_screen

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-f", "--file", help="CSV file to save output")

    args = parser.parse_args()

    ids = fetch_id(args.query)
    articles = fetch_details(ids)

    results = [parse_article(a) for a in articles]

    if args.file:
        save_to_file(results, args.file)
    else:
        print_to_screen(results)

if __name__ == "__main__":
    main()
