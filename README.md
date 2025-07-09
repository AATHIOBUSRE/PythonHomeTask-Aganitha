# get-papers-pubmed

This is a command-line tool I built to fetch research papers from PubMed, but with a focus on filtering papers that have at least one author working in a pharmaceutical or biotech company.

It helps you find industry-backed research easily from a large list of results.

---

## What this tool does

You give a search query like `"cancer immunotherapy"`, and it fetches papers from PubMed using their API. Then it checks the authors and tries to identify if anyone is from a company (not a university). Finally, it collects all the details and shows them to you or saves them to a CSV file.

The output includes:
- PubMed ID
- Title
- Publication Date
- Names of authors from companies
- Company affiliations
- Corresponding author's email (if found)

---

## What I used

I used Python 3.9 to build everything.

For accessing PubMed, I used **Biopython**, because it has a simple way to fetch papers from PubMed using their Entrez API.

To manage dependencies, create CLI commands, and publish the package, I used **Poetry**. It helped me create the script easily and allowed me to publish the package to TestPyPI.

For version control, I used **Git** and uploaded everything to my GitHub repo.

---

## External websites I used

- [PubMed](https://pubmed.ncbi.nlm.nih.gov): The main source where I fetch the papers.
- [TestPyPI](https://test.pypi.org): To test publishing my package before uploading to the real PyPI.
- [GitHub](https://github.com/AATHIOBUSRE/PythonHomeTask-Aganitha): I pushed my code here.
- [Poetry Documentation](https://python-poetry.org): I followed this to learn how to build and publish a package.

---

## How LLMs helped me

I used **ChatGPT** while building this project. I didn't copy code blindly — I asked questions like:

- “How to structure a Python package with CLI using Poetry?”
- “How to use Biopython to fetch articles from PubMed?”
- “How to detect if an author is from a company?”
- “What to write in a proper README?”
- “How to fix errors when publishing to TestPyPI?”

It really helped me understand the workflow better, and I learned how to debug issues step by step. All the final code and structure I tried to do on my own, just with guidance when I got stuck.

---

## How to install (from TestPyPI)

If you're testing it from TestPyPI:

pip install -i https://test.pypi.org/simple get-papers-pubmed
Or you can run it locally using Poetry.

How to use
After installing, you can run:

get-papers-list "covid vaccine"
If you want to save the output to a file:


get-papers-list "covid vaccine" -f output.csv
If you want to see help:


get-papers-list --help
You can also add --debug if you want to see what’s happening inside while it runs.

Running locally
Clone my repo and install dependencies:

git clone https://github.com/AATHIOBUSRE/PythonHomeTask-Aganitha.git
cd PythonHomeTask-Aganitha
poetry install
Run the tool like this:

poetry run get-papers-list "your query here"
About me
I'm AATHIOBUSRE. I made this project as part of a task, but I also wanted to learn how Python packaging and publishing works.

Email: aathiobusre@gmail.com
GitHub: https://github.com/AATHIOBUSRE

License
MIT License — you’re free to use, share, and improve it.

yaml
Copy
Edit

---

Let me know if you want this copied into a `README.md` file directly or pushed to your GitHub!
