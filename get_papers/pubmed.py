from Bio import Entrez
Entrez.email = "aathiobusre@gmail.com"
def fetch_id(query):
    handle = Entrez.esearch(db="pubmed", retmax=10,term="query")
    record = Entrez.read(handle)
    return record['IdList']
def fetch_details(IdList):
    ids = ",".join(IdList)
    handle = Entrez.efetch(db="pubmed", id=ids, retmode="xml")
    records = Entrez.read(handle)     
    records = records['PubmedArticle'] 
    return records

# query = "Cancer vaccine"
# id = fetch_id(query)
# details = fetch_details(id)
# for article in details:
#     info = parse_article(article)
#     print(info)