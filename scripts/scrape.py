# Modified template given by MAST30034
import pandas as pd
import lxml
# read in the postcode data from: https://www.matthewproctor.com/australian_postcodes
aus_pos = pd.read_csv("../data/raw/australian_postcodes.csv", usecols = ['postcode','locality','state'], header =0)
#keep only necessary information
aus_pos = aus_pos.iloc[:,:4]
# get rid of all other states other than victoria
vic_post = aus_pos.loc[aus_pos['state'] == 'VIC']
vic_post_uniq = vic_post['postcode'].unique().tolist()
# built-in imports
import re
from json import dump

from collections import defaultdict

# user packages
from bs4 import BeautifulSoup
import requests
import numpy as np
import math
import random
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import concurrent.futures
url_links = []
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
requests_session = requests.Session()
BASE_URL = "https://www.domain.com.au"
# First to create all the base pages to create list for the multithreading:
main_urls = []
NUM_THREADS = 10
# takes in postcode[0] and fetches all the links for it
def get_main_urls(postcode):
    url = BASE_URL +  f"/rent/?postcode={postcode}&sort=default-desc"
    bs_object = BeautifulSoup(requests_session.get(url, headers=headers).text, "lxml")
    time.sleep(1)
    result = bs_object \
        .find(
            "h1",
            {"data-testid": "summary","class":"css-ekkwk0"}
        )
    if result is not None:
        result_count = int(result.text.split()[0])
        if result_count < 1000:
            num_pages = range(1,math.ceil(result_count/20)+1)
        else:
            num_pages = range(1,51)
        if result_count != 0:
            for page in num_pages:
                main_urls.append(BASE_URL +  f"/rent/?postcode={postcode}&sort=default-desc&page={page}")
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(get_main_urls, vic_post_uniq)
def get_property_urls(url):
    bs_object = BeautifulSoup(requests_session.get(url, headers=headers).text, "lxml")
    time.sleep(random.randint(2, 3))
    # find the unordered list (ul) elements which are the results, then
    # find all href (a) tags that are from the base_url website.
    index_links = bs_object \
        .find(
            "ul",
            {"data-testid": "results"}
        ) \
        .findAll(
            "a",
            href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
        )

    for link in index_links:
        # if its a property address, add it to the list
        if 'address' in link['class']:
            url_links.append(link['href'])
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(get_property_urls, main_urls)
property_metadata = defaultdict(dict)
def store_details(url):
    bs_object = BeautifulSoup(requests_session.get(url, headers=headers).text, "lxml")
    time.sleep(random.randint(2, 3))
    # looks for the header class to get property name
    property_metadata[url]['name'] = bs_object \
        .find("h1", {"class": "css-164r41r"}) \
        .text

    property_metadata[url]['prop_type'] = bs_object \
        .find("div", {"data-testid": "listing-summary-property-type"}) \
        .text
    # looks for the div containing a summary title for cost
    property_metadata[url]['cost_text'] = bs_object \
        .find("div", {"data-testid": "listing-details__summary-title"}) \
        .text

    # extract coordinates from the hyperlink provided
    # i'll let you figure out what this does :P
    property_metadata[url]['coordinates'] = [
        float(coord) for coord in re.findall(
            r'destination=([-\s,\d\.]+)', # use regex101.com here if you need to
            bs_object \
                .find(
                    "a",
                    {"target": "_blank", 'rel': "noopener noreferer"}
                ) \
                .attrs['href']
        )[0].split(',')
    ]

    property_metadata[url]['rooms'] = [
        re.findall(r'\d\s[A-Za-z]+', feature.text) for feature in bs_object \
            .find("div", {"data-testid": "property-features"}) \
            .findAll("span", {"data-testid": "property-features-text-container"})
    ]

    if bs_object.find("ul", {"class":"css-4ewd2m"}) is not None:
        property_metadata[url]['add_feat'] = [
            re.sub(r'[^\w\s]', '', feature.text)  for feature in bs_object.find("ul", {"class":"css-4ewd2m"})
        ]
    else:
        property_metadata[url]['add_feat'] = ["No Extra Features Listed"]
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(store_details, url_links)
# Output saved data to raw folder
with open('../data/raw/domain_scraped_raw.json', 'w') as f:
    dump(property_metadata, f)
