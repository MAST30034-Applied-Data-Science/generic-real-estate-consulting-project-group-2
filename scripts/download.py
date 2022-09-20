import requests

# Download school data
file_link = "https://www.education.vic.gov.au/Documents/about/research/datavic/dv309_schoollocations2021.csv"
r = requests.get(file_link)
path = "../data/raw/australia_school"
with open(path,'wb') as p:
    p.write(r.content)

