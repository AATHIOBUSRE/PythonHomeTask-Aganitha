import re

def parse_article(article):
    info = {}

    info["PubmedID"] = article["MedlineCitation"]["PMID"]
    info["Title"] = article["MedlineCitation"]["Article"]["ArticleTitle"]

    pub_date = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]
    info["Publication Date"] = str(pub_date)

    authors = article["MedlineCitation"]["Article"].get("AuthorList", [])
    non_acad = []
    companies = []
    email = ""

    for author in authors:
        name = author.get("LastName", "")
        aff_info = author.get("AffiliationInfo", [])
        aff = aff_info[0].get("Affiliation", "") if aff_info else ""

        
        if "university" not in aff.lower():
            non_acad.append(name)

        if "Pharma" in aff or "Inc" in aff or "Ltd" in aff:
            companies.append(aff)

        match = re.search(r"\S+@\S+", aff)
        if match and not email:
            email = match.group(0)

    info["Non-academic Author(s)"] = "; ".join(non_acad)
    info["Company Affiliation(s)"] = "; ".join(companies)
    info["Corresponding Author Email"] = email

    return info
