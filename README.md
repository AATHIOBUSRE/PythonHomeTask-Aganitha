# get-papers

A simple command-line tool to fetch PubMed research papers using a user query, and list only those with at least one author affiliated with a **pharmaceutical** or **biotech** company.

This tool was built using the Entrez API from **BioPython** and packaged using **Poetry**. It supports saving the results to a CSV file or printing them to the screen.

---

## 🚀 Features

- Fetch papers from PubMed using any query
- Extract:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Authors
  - Company Affiliations
  - Corresponding Author Email
- Print or save results to CSV
- Supports debug mode for development
- Packaged as a CLI tool using Poetry

---

## 📦 Installation (Development Mode)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/get-papers.git
cd get-papers
