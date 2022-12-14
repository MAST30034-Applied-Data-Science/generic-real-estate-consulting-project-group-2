# Generic Real Estate Consulting Project
- Group 2: Andy Ng(1170648), Yuhao Zhai(1067899), Yun Keng Leong (1133704), Qianzhe Cheng (1174163)

**Research Goal:** The research goal is to find the affecting properties on the rental prices for both residential properties and apartments throughout Victoria.

**Timeline:** The timeline for the research area is current year for rental pricing and 2001-2021 for population forecasting.

Visit the `scripts` directory to run the files 1-2, `model` directory for file 5, and `notebook` directory to run all other files:
1. `download.py`: This script is for downloading external dataset.
2. `scrape.py`: This script is for data scraping.
3. `Rental_Preprocessing.ipynb`: This notebook is for preprocessing the scraped rental data.
4. `Preprocess.ipynb`: This notebook is to preprocess external datasets found.
5. `Internal_External_Analysis.ipynb`: This notebook is to analyse the important features that contribute to price
6. `population_forecast2.ipynb`: This notebook is for population forecasting.
7. `postcode_population.ipynb`: This notebook is for postcode population forecasting.
8. `Proximity_calculation.ipynb`: This notebook is for finding the proximity of amenities to rental properties
9. `suburb_growth_rate_sort.ipynb`: This notebook is to find the top suburb grow rate.
10. `Livability_Affordability.ipynb`: This notebook calculates the livability and affordability of various suburbs
11. `Summary_Notebook.ipynb`: This notebook summarizes our approach, analysis and issues/ difficulties throughout the project

**Scraped or Calulated Data:**<br />
`domain_scraped_raw.json`: Scraped rental property data from domain.com <br />
`proximty_calc_final.csv`: File containing all the proximity calculations made using On-Premise OpenRouteService

**External Datasets:**<br />
Notes on directory `generic-real-estate-consulting-project-group-2/data/raw/`: Some datasets that could be downloaded through writing a script has been written in the `download.py` script. However, there are a few amount of datasets that can only be downloaded manually, these datasets are uploaded manually to the github repository. Some links have been attached down below for those datasets that are downloaded manually. 

Links to the external datasets that are downloaded manually:<br />
`income`: https://explore.data.abs.gov.au/vis?fs[0]=Labour%2C0%7CEarnings%20and%20work%20hours%23EARNINGS_HOURS%23&pg=0&fc=Labour&df[ds]=LABOUR_TOPICS&df[id]=AWE&df[ag]=ABS&df[vs]=1.0.0&pd=2020-Q1%2C&dq=1.1.3.7....Q&ly[cl]=TIME_PERIOD&ly[rw]=REGION%2CINDUSTRY&ly[rs]=TSEST <br />
`population`: https://explore.data.abs.gov.au/vis?fs[0]=People%2C0%7CPopulation%23POPULATION%23&pg=40&fc=People&df[ds]=PEOPLE_TOPICS&df[id]=ERP_Q&df[ag]=ABS&df[vs]=1.0.0&pd=2019-Q2%2C&dq=1.3.TOT..Q&ly[cl]=TIME_PERIOD&ly[rw]=REGION <br />
`household income`: https://explore.data.abs.gov.au/vis?pg=0&tm=income%20sa2&df[ds]=CENSUS_2021_TOPICS&df[id]=C21_G33_SA2&df[ag]=ABS&df[vs]=1.0.0&pd=2021%2C&dq=..AUS..&ly[cl]=HHCD&ly[rw]=HIND <br />
`recre_fal`: CSV of recreational facility locations and other details: https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fdiscover.data.vic.gov.au%2Fdataset%2Fe6db797e-3801-4cfa-bf02-82350d0f722d%2Fresource%2Fbfff5fff-9c74-4671-8396-43f793613b70%2Fdownload%2Fsrv_ifmd_all-facilities.xlsx&wdOrigin=BROWSELINK <br />
`income_suburb`: https://data.gov.au/data/dataset/taxation-statistics-2019-20/resource/50bad443-39eb-4f60-bce5-d2978fc61e1b?inner_span=True <br />
`hospital_data`: Folder of shapefiles for hospital locationscollected from qgis query for amenities:hospital <br /> `shopping_data`: Folder of shapefiles for shopping lcoations collected from qgis query for shops/food, shops/general, shops/convinence <br />
`TRANSPORT`: Folder of shapefiles for train locations ordered from https://discover.data.vic.gov.au/dataset/victorian-railway-stations <br />
`rental_zones`: Folder of shapefiles for boundaries ordered from: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files <br />
`locality`: Folder of shapefiles for suburb boundaries ordered from: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files
